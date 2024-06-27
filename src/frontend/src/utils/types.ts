export type Team = {
    id: string,
    name: string,
    has_website: boolean,
    total_score: number
}

export type History = {
    [key: string]: number
}

export type Scenario = {
    id: number,
    name: string
}

export type Result = {
    id: string,
    scenario: number,
    status: "FAILED" | "DONE" | "PENDING"
    score: number,
    average_time: number
}

export type PlaceholderResult = {
    score: string,
    status: string,
    average_time: string
}