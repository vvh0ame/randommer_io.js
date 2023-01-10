import requests

class RandommerIO:
	def __init__(self, api_key: str) -> None:
		self.api = "https://randommer.io/api"
		self.headers = {
			"x-api-key": api_key,
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}
		self.api_key = api_key

	def get_card(self, type: str) -> dict:
		return requests.get(
			f"{self.api}/Card?type={type}",
			headers=self.headers).json()

	def get_card_types(self) -> list[str]:
		return requests.get(
			f"{self.api}/Card/Types",
			headers=self.headers).json()

	def get_crypto_types(self) -> list[str]:
		return requests.get(
			f"{self.api}/Finance/CryptoAddress/Types",
			headers=self.headers).json()

	def get_crypto_address(
			self,
			crypto_type: str) -> dict:
		return requests.get(
			f"{self.api}/Finance/CryptoAddress?cryptoType={crypto_type}",
			headers=self.headers).json()

	def get_iban_by_country_code(
			self,
			country_code: str) -> str:
		return requests.get(
			f"{self.api}/Finance/Iban/{country_code}",
			headers=self.headers).json()

	def get_finance_countries(self) -> list[dict]:
		return requests.get(
			f"{self.api}/Finance/Countries",
			headers=self.headers).json()

	def validate_vat(
			self,
			country: str,
			vat: str) -> dict:
		return requests.post(
			f"{self.api}/Finance/Vat/Validator?country={country}&vat={vat}",
			headers=self.headers).json()

	def get_misc_cultures(self) -> list[dict]:
		return requests.get(
			f"{self.api}/Misc/Cultures",
			headers=self.headers).json()

	def get_misc_random_address(
			self,
			number: int,
			culture: str = "en") -> list[str]:
		return requests.get(
			f"{self.api}/Misc/Random-Address?number={number}&culture={culture}",
			headers=self.headers).json()

	def get_name(
			self,
			name_type: str,
			quantity: int) -> list[str]:
		"""
		Get the list of strings that contains random names

		Parameters:
			name_type: (str): string <firstname, surname, fullname>
			quantity: (int): integer <int32>

		Returns: 
			list[str]: the list of strings that contains random names
		"""
		return requests.get(
			f"{self.api}/Name?nameType={name_type}&quantity={quantity}",
			headers=self.headers).json()

	def get_business_name_suggestions(
			self,
			starting_words: str) -> list[str]:
		return requests.get(
			f"{self.api}/Name/Suggestions?startingWords={starting_words}",
			headers=self.headers).json()

	def get_name_cultures(self) -> list[dict]:
		return requests.get(
			f"{self.api}/Name/Cultures",
			headers=self.headers).json()

	def get_culture_business_name(
			self,
			number: int,
			culture_code: str) -> list[str]:
		"""
		Get the list of strings that contains business names for specific culture

		Parameters:
			number: (int): integer <int32>
			culture_code: (str): string <default: en_US>

		Returns: 
			list[str]: the list of strings that contains business names for specific culture
		"""
		return requests.post(
			f"{self.api}/Name/BusinessName?number={number}&cultureCode={culture_code}",
			headers=self.headers).json()

	def get_brand_name_suggestions(
			self,
			starting_words: str) -> list[str]:
		return requests.get(
			f"{self.api}/Name/BrandName?startingWords={starting_words}",
			headers=self.headers).json()

	def get_country_phone_numbers(
			self,
			country_code: str,
			quantity: int) -> list[str]:
		return requests.get(
			f"{self.api}/Phone/Generate?countryCode={country_code}&Quantity={quantity}",
			headers=self.headers).json()

	def get_bulk_imeis(
			self,
			quantity: int) -> list[dict]:
		return requests.get(
			f"{self.api}/Phone/IMEI?Quantity={quantity}",
			headers=self.headers).json()

	def validate_phone_number(
			self,
			phone_number: str,
			country_code: str) -> dict:
		return requests.get(
			f"{self.api}/Phone/Validate?telephone={phone_number}&countryCode={country_code}",
			headers=self.headers).json()

	def get_phone_countries(self) -> list[dict]:
		return requests.get(
			f"{self.api}/Phone/Countries",
			headers=self.headers).json()

	def get_social_security_number(self) -> str:
		return requests.get(
			f"{self.api}/SocialNumber",
			headers=self.headers).json()

	def get_lorem_ipsum(
			self,
			lorem_type: str,
			type: str,
			number: int) -> str:
		"""
		Get lorem ipsum text words or paragraphs

		Parameters:
			lorem_type: (str): string <normal, business>
			type: (str): string <paragraphs, words>
			number: (int): integer <int32>

		Returns: 
			str: lorem ipsum text words or paragraphs
		"""
		return requests.get(
			f"{self.api}/Text/LoremIpsum?loremType={lorem_type}&type={type}&number={number}",
			headers=self.headers).json()

	def generate_password(
			self,
			length: int,
			has_digits: bool,
			has_uppercase: bool,
			has_special: bool) -> str:
		return requests.get(
			f"{self.api}/Text/Password?length={length}&hasDigits={has_digits}&hasUppercase={has_uppercase}&hasSpecial={has_special}",
			headers=self.headers).json()
