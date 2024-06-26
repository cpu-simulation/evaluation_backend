import { Team } from "./utils/types";

export async function getTeams() {
    try {
        const res = await fetch(`/evaluation/teams`)
        const teams = await res.json()
        return teams
    } catch (err: any) {
        console.log(err)
        throw new Error(err)
    }
}

export async function getResults(team: Team) {
    try {
        const res = await fetch(`/evaluation/results/${team.id}`)
        const results = await res.json()
        return results
    } catch (err: any) {
        console.log(err)
        throw new Error(err)
    }
}

export async function getHistory(team: Team) {
    try {
        const res = await fetch(`/evaluation/history/${team.id}`)
        const results = await res.json()
        return results
    } catch (err: any) {
        console.log(err)
        throw new Error(err)
    }
}


export async function getScenarios() {
    try {
        const res = await fetch(`/evaluation/scenarios`)
        const results = await res.json()
        return results
    } catch (err: any) {
        console.log(err)
        throw new Error(err)
    }
}

export async function runTests(team: Team) {
    try {
        await fetch(`/evaluation/test/${team.id}`, {
            method: "POST"
        })
    } catch (err: any) {
        console.log(err)
        throw new Error(err)
    }
}