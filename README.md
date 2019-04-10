

# Weather API demo

Providing an easy to use tool for Customers/developers/QA teams to retrieve weather information by API using
openweathermap service. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Cloning the project
```
git clone https://github.com/IlanZuckerman/weather_api.git
```

### Prerequisites

Python 3.7

Needed packages are listed in requirements.txt under root of this project.
In order to install those packages, use the following command:
```
$ pip install -r requirements.txt
```

## Running from command line examples

1) To get current weather conditions for London city: 
```
> python demo.py -p -c "London"
```
2. To get current weather conditions for London by city ID:
```
> python demo.py -p -i "524901"
```
3. To get 6 hours forecast in London:
```
> python demo.py -p -f -cnt "2" -c "London"
```
4. To get 3 hours forecast in London by city ID:
```
> python demo.py -p -f -cnt "1" -i "524901"
```

## Contributing


## Authors
Ilan Zuckerman

## License


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
