import express from 'express'
const app = express()
const PORT = process.env.PORT || 3000
import * as data from './data.js'

app.listen(PORT, () => {
    console.log(`listening on port ${PORT}`)
})

app.use(express.static('dist'))
app.use(express.json())

app.get("/api/v1", (req, res) => { res.json({ message: "Hello from server!" }) })

app.get("/api/v1/teams", (req, res) => {
    res.json(data.teams)
})

app.get("/api/v1/evaluation/results", (req, res) => {
    console.log(req.query)
    const r = data.results.map(result => {
        result.average_time = (Math.random() * 8).toFixed(2)
        result.score = parseInt(Math.random() * 8)
        result.status = ["FAILED", "PENDING", "DONE"][parseInt(Math.random() * 3 - 0.01)]
        return result
    })
    res.json(r)
})

app.get("/api/v1/evaluation/scenarios", (req, res) => {
    res.json(data.scenarios)
})

app.get("/api/v1/team/:id/history", (req, res) => {
    res.json(data.history)
})


app.post("/api/v1/team/:id/test", (req, res) => {
    console.log("testing team:", req.params.id)
    res.status(200).send()
})

// If user requested something other than APIs then it will be handled by the UI
app.use('/*', (req, res) => {
    res.sendFile('index.html', { root: 'dist' }, function (err) {
        if (err) {
            res.status(500).send(err)
        }
    })
})