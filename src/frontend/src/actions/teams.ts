import { teams } from "../utils/data";

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

export async function getTeams() {
    await sleep(500)
    return teams
}