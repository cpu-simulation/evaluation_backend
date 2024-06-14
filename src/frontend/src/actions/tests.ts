import { results, scenarios } from "../utils/data"
import { Team } from "../utils/types";

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

export async function getResults(team: Team) {
    await sleep(500)
    results[0].average_time = parseFloat((Math.random() * 5).toPrecision(3))
    return results
}

export async function getScenarios() {
    await sleep(500)
    return scenarios
}