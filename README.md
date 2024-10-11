# randommer_io.js
Web-API for [randommer.io](https://randommer.io) website to generate random stuff

## Example
```JavaScript
async function main() {
	const { RandommerIo } = require("./randommer_io.js")
	const randommerIo = new RandommerIo("apiKey")
	const card = await randommerIo.getCar("type")
  console.log(card(
}

main()
```
