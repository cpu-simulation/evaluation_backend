import { Team } from "./utils/types";

export async function getTeams() {
    try {
        const res = await fetch("/api/v1/teams")
        const teams = await res.json()
        return teams
    } catch (err: any) {
        console.log(err)
        throw new Error(err)
    }
}

export async function getResults(team: Team) {
    try {
        const res = await fetch(`/api/v1/evaluation/results/?team=${team.id}`)
        const results = await res.json()
        return results
    } catch (err: any) {
        console.log(err)
        throw new Error(err)
    }
}

export async function getHistory(team: Team) {
    try {
        const res = await fetch(`/api/v1/team/${team.id}/history`)
        const results = await res.json()
        return results
    } catch (err: any) {
        console.log(err)
        throw new Error(err)
    }
}


export async function getScenarios() {
    try {
        const res = await fetch("/api/v1/evaluation/scenarios")
        const results = await res.json()
        return results
    } catch (err: any) {
        console.log(err)
        throw new Error(err)
    }
}

export async function runTests(team: Team) {
    try {
        await fetch(`/api/v1/team/${team.id}/test`, {
            method: "POST"
        })
    } catch (err: any) {
        console.log(err)
        throw new Error(err)
    }
}