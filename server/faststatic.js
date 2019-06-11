const express = require('express')
const app = express()
const port = 80

console.log(`starting at 134.209.206.33`)
app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))

app.use('/static', express.static('static'))
