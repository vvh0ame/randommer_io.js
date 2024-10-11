class RandommerIo {
	constructor(apiKey) {
		this.api = "https://randommer.io/api"
		this.headers = {
			"x-api-key": apiKey,
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}
		this.apiKey = apiKey
	}

	async getCard(type) {
		const response = await fetch(
			`${this.api}/Card?type=${type}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCardTypes() {
		const response = await fetch(
			`${this.api}/Card/Types`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCryptoTypes() {
		const response = await fetch(
			`${this.api}/Finance/CryptoAddress/Types`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCryptoAddress(cryptoType) {
		const response = await fetch(
			`${this.api}/Finance/CryptoAddress?cryptoType=${cryptoType}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getIbanByCountryCode(countryCode) {
		const response = await  fetch(
			`${this.api}/Finance/Iban/${countryCode}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getFinanceCountries() {
		const response = await fetch(
			`${this.api}/Finance/Countries`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async validateVac(country, vac) {
		const response = await fetch(
			`${this.api}/Finance/Vat/Validator?country=${country}&vat=${vat}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getMiscCultures() {
		const response = await fetch(
			`${this.api}/Misc/Cultures`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getNameCultures() {
		const response = await fetch(
			`${this.api}/Name/Cultures`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}
 }

module.exports = {RandommerIo}
