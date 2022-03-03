from flask import current_app, request

from app.models.state_models import States


def create_state(state):
    session = current_app.db.session()
    state_db: States = States.query.filter_by(name = state).one_or_none()

    if not state_db:
        state_db = States(name = state)
        session.add(state_db)
        session.commit()


    return state_db.state_id