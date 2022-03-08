# rental-cars-api

#### Plataforma de gerenciamento de locadora de veículos.

#

**Links**
api: https://rental-cars-api.herokuapp.com/

#

### End-Points

1. Users
2. Address_user
3. Rental_cars
4. Cars
5. States
6. Categories
7. Maintenance_car

---

-   ### Users

* Cadastro de cliente.


|   url    | metodo |   status    |
| :------: | :----: | :---------: |
| `/users` | `Post` | `201` |

**Body** - `json`

```
{
	"cnh": "12345678910",
	"cpf": "12345678910",
	"name": "Jhon Doe",
	"email": "mail@mail.com",
	"phone": "80123456789",
	"category_cnh": "B",
	"address": {
	    "street": "Rio Claro",
	    "number": "233",
	    "district": "Riachino",
	    "zip_code": "32340100",
	    "city": "Contagem Grande",
	    "reference": "esquina do v",
	    "state": "Bahia"
	}
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
	"category_cnh": "B",
	"user_address": [
		{
			"id": 3,
			"street": "Rio Claro",
			"number": "233",
			"district": "Riachino",
			"zip_code": "32340100",
			"city": "Contagem Grande",
			"reference": "esquina do v",
			"state": "Bahia"
		}
	]
}
```
* Consultar todos os clientes cadastrados

|   url    | metodo |   status    |
| :------: | :----: | :---------: |
| `/users` | `Get`  | `200` |

**Response** - `json`

```
{
	"cnh": "12345678910",
	"cpf": "12345678910",
	"name": "Jhon Doe",
	"email": "mail@mail.com",
	"phone": "80123456789",
	"category_cnh": "B",
	"user_address": [
		{
			"id": 3,
			"street": "Rio Claro",
			"number": "233",
			"district": "Riachino",
			"zip_code": "32340100",
			"city": "Contagem Grande",
			"reference": "esquina do v",
			"state": "Bahia"
		}
	]
}
```

* Consultar cliente por CNH

|   url    | metodo |   status    |
| :------: | :----: | :---------: |
| `/users/cnh` | `Get`  | `200` |

**Response** - `json`

```
{
	"cnh": "12345678910",
	"cpf": "12345678910",
	"name": "Jhon Doe",
	"email": "mail@mail.com",
	"phone": "80123456789",
	"category_cnh": "B",
	"user_address": [
		{
			"id": 3,
			"street": "Rio Claro",
			"number": "233",
			"district": "Riachino",
			"zip_code": "32340100",
			"city": "Contagem Grande",
			"reference": "esquina do v",
			"state": "Bahia"
		}
	]
}
```

* Atualizar dados do cliente

|   url    | metodo |   status    |
| :------: | :----: | :---------: |
| `/users/12345678910` | `Patch`  | `200` |

**Body** - `json`

```
{
	"cnh": "12345678911",
	"cpf": "12345678911",
	"name": "Jhon Dooe",
	"email": "othermail@mail.com",
	"phone": "80123459876",
	"category_cnh": "AB",
	"address": {
	    "street": "Cantagalo",
	    "number": "235",
	    "district": "Riacho",
	    "zip_code": "32340110",
	    "city": "Contagem",
	    "reference": "esquina da praça",
	    "state": "Minas Gerais"
	}
}
```
**Response** - `json`

```
{
  "cnh": "12345678910",
  "cpf": "12345678910",
  "name": "Jhon Dooe",
  "email": "othermail@mail.com",
  "phone": "80123459876",
  "category_cnh": "AB",
  "user_address": [
    {
      "address_id": 4,
      "street": "Cantagalo",
      "number": "235",
      "district": "Riacho",
      "zip_code": "32340110",
      "city": "Contagem",
      "reference": "esquina da praça",
      "state": "Minas Gerais"
    }
  ]
}

```
**OBS: CNH e CPF não podem ser alterados**

---

-   ### Address_user
  
*    Cadastrar um endereço .

Endereço será cadastrado juntamente com o corpo da requisição do cliente, caso o endereço já exista será retornado o id do endereço caso contrário o endereço será cadastrado

*	Buscar por endereços

|    url     | metodo | status |
| :--------: | :----: | :----: |
| `/addresss` | `Get` | `200`  |

**Response** - `json`

```
[
	{
		"Minas Gerais":[
			{
				"address_id": 1,
				"street": "Rio Comprido",
				"number": "235",
				"district": "Riacho",
				"zip_code": "32340100",
				"city": "Contagem",
				"reference": "esquina",
				"state_id": 1
			}
		]
	},
	{
		"Bahia": [
			{
				"address_id": 2,
				"street": "Rio Curto",
				"number": "233",
				"district": "Riacho",
				"zip_code": "32340100",
				"city": "Contagem",
				"reference": "esquina",
				"state_id": 2
			}
		]
	}	
]

```

*	Atualização de endereço

	Caso ocorrer atualização de endereço de usuário, será adicionado ao banco o novo endereço, não será atualizado, pois pode haver mais de um usuário utilizando o mesmo endereço 


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

	Estado será cadastrado juntamente com o corpo da requisição do cliente, caso o estado já exista será retornado o id do estado na tabela de endereços caso contrário o estado será cadastrado

---

-   ### Category_car

*   Cadastrar uma categoria de um veículo

|   url   | metodo |   status    |
| :-----: | :----: | :---------: |
| `/categories` | `Post`  | `200` |


**Body** - `json`

```

{
    "body_types": "Sedan",
    "fuel_type": "Gasolina",
    "engine_power": "116 cv",
    "km_per_liter": 10.8,
    "allowed_category_cnh": "B",
    "differentials": "vidro e trava elétricos"
}

```

**Response** - `json`

```
{
  "category_id": 1,
  "body_types": "Sedan",
  "fuel_type": "Gasolina",
  "engine_power": "116 cv",
  "km_per_liter": 10.8,
  "allowed_category_cnh": "B",
  "differentials": "vidro e trava elétricos"
}
```

---

-   ### Maintenance_car


*   Criar uma manutenção

|   url   | metodo |   status    |
| :-----: | :----: | :---------: |
| `/maintenance` | `Post`  | `201` |

**Body** - `json`

```
{
    "last_maintenance": "03/01/2022",
    "next_maintenance": "03/03/2022",
    "repaired_items": ["pastilha de freio", "fluido de freio", "óleo"],
    "maintenance_price": 250.84
}
```

**Response** - `json`

```
{
  "maintenance_id": 1,
  "last_maintenance": "03/01/2022",
  "next_maintenance": "03/03/2022",
  "repaired_items": "{\"pastilha de freio\",\"fluido de freio\",óleo}",
  "maintenance_price": 250.84
}

```

* Listar as manutenções

|   url   | metodo |   status    |
| :-----: | :----: | :---------: |
| `/maintenance/id` | `Get`  | `200 - 400` |

**Response** - `json`

```
{
  "maintenance_id": 1,
  "last_maintenance": "03/01/2022",
  "next_maintenance": "03/03/2022",
  "repaired_items": "{\"pastilha de freio\",\"fluido de freio\",óleo}",
  "maintenance_price": 250.84
}

```

*   Atualizar os dados de uma manutenção

|   url   | metodo |   status    |
| :-----: | :----: | :---------: |
| `/maintenance/id` | `Patch`  | `201` |

**Body** - `json`

```
{
    "last_maintenance": "02/01/2022",
    "next_maintenance": "03/04/2022",
    "repaired_items": ["pastilha de freio", "fluido de freio", "óleo, correia dentada"],
    "maintenance_price": 310.92
}
```

**Response** - `json`

```
{
  "maintenance_id": 1,
  "last_maintenance": "02/01/2022",
  "next_maintenance": "03/04/2022",
  "repaired_items": "{\"pastilha de freio\",\"fluido de freio\",\"óleo, correia dentada\"}",
  "maintenance_price": 310.92
}

```
---