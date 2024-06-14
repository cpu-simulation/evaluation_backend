import { Result, Scenario, Team } from "./types";

export const teams: Team[] = [
    {
        id: "",
        name: "Team A",
        type: "website",
        total_score: 1,
    },
    {
        id: "",
        name: "Team B",
        type: "website",
        total_score: 3,
    },
    {
        id: "",
        name: "Team C",
        type: "website",
        total_score: 4,
    },
    {
        id: "",
        name: "Team D",
        type: "website",
        total_score: 2,
    },
    {
        id: "",
        name: "Team E",
        type: "webiste",
        total_score: 7,
    },
    {
        id: "",
        name: "Team F",
        type: "core",
        total_score: 6,
    },
    {
        id: "",
        name: "Team G",
        type: "core",
        total_score: 5,
    },
    {
        id: "",
        name: "Team H",
        type: "core",
        total_score: 8,
    },
    {
        id: "",
        name: "Team I",
        type: "core",
        total_score: 9
    }
]

export const scenarios: Scenario[] = [
    {
        id: 0,
        name: "Test 1",
    },
    {
        id: 1,
        name: "Test 2",
    },
    {
        id: 2,
        name: "Test 3",
    },
    {
        id: 3,
        name: "Test 4",
    },
    {
        id: 4,
        name: "Test 5",
    }
]

export const results: Result[] = [
    {
        id: "1234",
        state: "PASSED",
        score: 4,
        average_time: 1.2,
        scenario: 0
    }
]