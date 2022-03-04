# rental-cars-api

#### Plataforma de gerenciamento de locadora de veículos.

#

**Links**
api: https://www.heroku.com/
<!-- [Documentação Projeto](https://) -->

#

### End-Points

1. Users
2. Address_user
3. Rental_cars
4. Cars
5. States
6. Categoria
7. Maintenance_car

---

-   ### Users

Cadastro de cliente (pessoa física ou jurídica que vai alugar os veículos).

**Clientes CNH**

|    url    | metodo |   status    |
| :-------: | :----: | :---------: |
| `/users` | `Post` | `200 - 400` |

**Body** - `json`

```
{
	"cnh": "12345678910",
	"cpf": "12345678910",
	"name": "Jhon Doe",
	"email": "mail@mail.com",
	"phone": "80123456789",
	"categorie_cnh": "B"
}
```

**Response** - `json`

```
{
	"cnh": "12345678910",
	"cpf": "12345678910",
	"name": "Jhon Doe",
	"email": "mail@mail.com",
	"phone": "80123456789",
	"categorie_cnh": "B"
}
```

**Clientes CNPJ**

**Body** - `json`

```
{
	"cliente": "cliente"
}
```

**Response** - `json`

```
{
	"cliente": "cliente"
}
```

|    url    | metodo |   status    |
| :-------: | :----: | :---------: |
| `/users` | `Get` | `200 - 400` |

**Response** - `json`

```
{
	"cnh": "12345678910",
	"cpf": "12345678910",
	"name": "Jhon Doe",
	"email": "mail@mail.com",
	"phone": "80123456789",
	"categorie_cnh": "B"
}
```
---

-   ### Address_user
    Cadastrar um endereço .

|    url    | metodo |   status    |
| :-------: | :----: | :---------: |
| `/address` | `Post` | `200 - 400` |

**Body** - `json`

```
{
	"xxx": "xxxxx"
}
```

**Response** - `json`

```
{
  	"xxx": "xxxx"
}
```

---

-   ### Rental_cars
    Cadastrar um carro pra alugar.

*   Cadastro de veículo

|    url    | metodo |   status    |
| :-------: | :----: | :---------: |
| `/xxxx` | `Post` | `200 - 400` |



**Body** - `json`

```
{
	"xxx": "xxxxxx",
	"xxxxx": "xxx"
}
```

**Response** - `json`

```
{
	"xxxx": "xxxx"
}
```

---

-   ### Cars
    Gerenciamento de carros.

*   Adiciobar o carro

|          url          | metodo |   status    |
| :-------------------: | :----: | :---------: |
| `/xxx` | `Post`  | `200 - 400` |


**Response** - `json`

```
{
	"xxx": "xxxxxx",
	"xxxxx": "xxx"
}
```
---

-   ### States
    Cadastro de  estados.

*   Buscar produto

|    url     | metodo |   status    |
| :--------: | :----: | :---------: |
| `/state` | `Post` | `200 - 400` |


**Body** - 
```
{
	"xxx": "xxxxxx",
	"xxxxx": "xxx"
}
```

**Response** - `json`

```
{
	"xxx": "xxxxxx",
	"xxxxx": "xxx"
}
```

---

-   ### Category_car
    Categoria do carro.

*   Listar carros

|     url      | metodo |   status    |
| :----------: | :----: | :---------: |
| `/xxxx` | `Get`  | `200 - 400` |


**Response** - `json`

```
```
{
	"xxx": "xxxxxx",
	"xxxxx": "xxx"
}


---

-   ### Maintenance_car
    Manutenção do carro.

*   Listar carros

|     url      | metodo |   status    |
| :----------: | :----: | :---------: |
| `/xxxx` | `Get`  | `200 - 400` |


**Response** - `json`

```
{
	"xxx": "xxxxxx",
	"xxxxx": "xxx"
}
---
