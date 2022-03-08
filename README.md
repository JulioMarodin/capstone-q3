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

|   url    | metodo |   status    |
| :------: | :----: | :---------: |
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

|   url    | metodo |   status    |
| :------: | :----: | :---------: |
| `/users` | `Get`  | `200 - 400` |

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

|    url     | metodo |   status    |
| :--------: | :----: | :---------: |
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
    Aluguel de veículos.

*   Alugar um veículo

|    url     | metodo | status |
| :--------: | :----: | :----: |
| `/rentals` | `Post` | `200`  |



**Body** - `json`

```
{
	"rental_date": "03/05/2022",
	"rental_return_date": "04/05/2022",
	"rental_total_days": 2,
	"customer_cnh": "12345678910",
	"car_license_plate": "ABC1234"
}
```

**Response** - `json`

```
{
	"rental_id": 1,
	"rental_date": "Thu, 03 May 2022 00:00:00 GMT",
	"rental_return_date": "Fri, 04 May 2022 00:00:00 GMT",
	"rental_real_return_date": null,
	"returned_car": false,
	"rental_total_days": 2,
	"rental_real_total_days": null,
	"initial_km": 610.0,
	"final_km": null,
	"total_fixed_km": 100,
	"total_returned_km": null,
	"rental_value": 200.0,
	"rental_real_value": null,
	"customer_cnh": "12345678910",
	"car_license_plate": "ABC1234"
}
```

*   Devolver um veículo

|    url     | metodo  | status |
| :--------: | :-----: | :----: |
| `/rentals` | `Patch` | `200`  |



**Body** - `json`

```
{
	"rental_real_return_date": "06/03/2022",
	"rental_real_total_days": 2,
	"total_returned_km": 610,
	"car_license_plate": "abc1234",
	"cnh": "12345678910"
}
```

**Response** - `json`

```
{
	"rental_id": 7,
	"rental_date": "Thu, 03 May 2022 00:00:00 GMT",
	"rental_return_date": "Fri, 04 May 2022 00:00:00 GMT",
	"rental_real_return_date": "Fri, 04 May 2022 00:00:00 GMT",
	"returned_car": true,
	"rental_total_days": 2,
	"rental_real_total_days": 2,
	"initial_km": 610.0,
	"final_km": 100.0,
	"total_fixed_km": 100,
	"total_returned_km": 710.0,
	"rental_value": 200.0,
	"rental_real_value": 200.0,
	"customer_cnh": "12345678910",
	"car_license_plate": "ABC1234"
}
```

*   Buscar todas as notas fiscais

|    url     | metodo | status |
| :--------: | :----: | :----: |
| `/rentals` | `Get`  | `200`  |


**Response** - `json`

```
[
	{
		"rental_id": 3,
		"rental_date": "Thu, 03 Mar 2022 00:00:00 GMT",
		"rental_return_date": "Fri, 04 Mar 2022 00:00:00 GMT",
		"rental_real_return_date": "Sun, 06 Mar 2022 00:00:00 GMT",
		"returned_car": true,
		"rental_total_days": 2,
		"rental_real_total_days": 4,
		"initial_km": 2.0,
		"final_km": 408.0,
		"total_fixed_km": 100,
		"total_returned_km": 410.0,
		"rental_value": 300.0,
		"rental_real_value": 860.0,
		"customer_cnh": "12345678910",
		"car_license_plate": "ABC1234"
	},
	{
		"rental_id": 5,
		"rental_date": "Thu, 03 Mar 2022 00:00:00 GMT",
		"rental_return_date": "Fri, 04 Mar 2022 00:00:00 GMT",
		"rental_real_return_date": "Sun, 06 Mar 2022 00:00:00 GMT",
		"returned_car": true,
		"rental_total_days": 2,
		"rental_real_total_days": 4,
		"initial_km": 410.0,
		"final_km": 200.0,
		"total_fixed_km": 100,
		"total_returned_km": 610.0,
		"rental_value": 300.0,
		"rental_real_value": 700.0,
		"customer_cnh": "12345678910",
		"car_license_plate": "ABC1234"
	}
]
```

*   Buscar aluguel atual do carro pela placa

|           url            | metodo | status |
| :----------------------: | :----: | :----: |
| `/rentals/plate/abc1234` | `Get`  | `200`  |


**Response** - `json`

```
{
    "rental_id": 3,
    "rental_date": "Thu, 03 Mar 2022 00:00:00 GMT",
    "rental_return_date": "Fri, 04 Mar 2022 00:00:00 GMT",
    "rental_real_return_date": "Sun, 06 Mar 2022 00:00:00 GMT",
    "returned_car": true,
    "rental_total_days": 2,
    "rental_real_total_days": 4,
    "initial_km": 2.0,
    "final_km": 408.0,
    "total_fixed_km": 100,
    "total_returned_km": 410.0,
    "rental_value": 300.0,
    "rental_real_value": 860.0,
    "customer_cnh": "12345678910",
    "car_license_plate": "ABC1234"
}
```

*   Buscar todos os alugueis pela cnh

|            url             | metodo | status |
| :------------------------: | :----: | :----: |
| `/rentals/all/12345678910` | `Get`  | `200`  |


**Response** - `json`

```
[
	{
		"rental_id": 3,
		"rental_date": "Thu, 03 Mar 2022 00:00:00 GMT",
		"rental_return_date": "Fri, 04 Mar 2022 00:00:00 GMT",
		"rental_real_return_date": "Sun, 06 Mar 2022 00:00:00 GMT",
		"returned_car": true,
		"rental_total_days": 2,
		"rental_real_total_days": 4,
		"initial_km": 2.0,
		"final_km": 408.0,
		"total_fixed_km": 100,
		"total_returned_km": 410.0,
		"rental_value": 300.0,
		"rental_real_value": 860.0,
		"customer_cnh": "12345678910",
		"car_license_plate": "ABC1234"
	},
	{
		"rental_id": 5,
		"rental_date": "Thu, 03 Mar 2022 00:00:00 GMT",
		"rental_return_date": "Fri, 04 Mar 2022 00:00:00 GMT",
		"rental_real_return_date": "Sun, 06 Mar 2022 00:00:00 GMT",
		"returned_car": true,
		"rental_total_days": 2,
		"rental_real_total_days": 4,
		"initial_km": 410.0,
		"final_km": 200.0,
		"total_fixed_km": 100,
		"total_returned_km": 610.0,
		"rental_value": 300.0,
		"rental_real_value": 700.0,
		"customer_cnh": "12345678910",
		"car_license_plate": "ABC1234"
	}
]
```

*   Buscar aluguel atual do carro pela cnh

|              url               | metodo | status |
| :----------------------------: | :----: | :----: |
| `/rentals/current/12345678910` | `Get`  | `200`  |


**Response** - `json`

```
{
	"rental_id": 7,
	"rental_date": "Thu, 03 Mar 2022 00:00:00 GMT",
	"rental_return_date": "Fri, 04 Mar 2022 00:00:00 GMT",
	"rental_real_return_date": "Sun, 06 Mar 2022 00:00:00 GMT",
	"returned_car": false,
	"rental_total_days": 2,
	"rental_real_total_days": 2,
	"initial_km": 610.0,
	"final_km": 0.0,
	"total_fixed_km": 100,
	"total_returned_km": 610.0,
	"rental_value": 20000.0,
	"rental_real_value": 20000.0,
	"customer_cnh": "12345678910",
	"car_license_plate": "ABC1234"
}
```

---

-   ### Cars
    Gerenciamento de carros.

*   Adiciobar o carro

|  url   | metodo |   status    |
| :----: | :----: | :---------: |
| `/xxx` | `Post` | `200 - 400` |


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

|   url    | metodo |   status    |
| :------: | :----: | :---------: |
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

|   url   | metodo |   status    |
| :-----: | :----: | :---------: |
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

|   url   | metodo |   status    |
| :-----: | :----: | :---------: |
| `/xxxx` | `Get`  | `200 - 400` |


**Response** - `json`

```
{
	"xxx": "xxxxxx",
	"xxxxx": "xxx"
}
---
