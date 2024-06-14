export type Team = {
    id: string,
    name: string,
    type: string,
    total_score: number
}

export type Scenario = {
    id: number,
    name: string
}

export type Result = {
    id: string,
    scenario: number,
    state: "WAITING" | "PASSED" | "FAILED"
    score: number,
    average_time: number
}

export type PlaceholderResult = {
    score: string,
    state: string,
    average_time: string
}