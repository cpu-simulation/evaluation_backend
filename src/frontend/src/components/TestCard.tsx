import { Result, Scenario, PlaceholderResult } from "../utils/types"

const r: PlaceholderResult = {
    score: "---",
    status: "---",
    average_time: "---"
}


function TestCard({ scenario, result = r, selected = false }:
    { selected?: boolean, result?: Result | PlaceholderResult, scenario: Scenario }) {
    return (
        <div onClick={() => { }}
            className={"test-card flex justify-between gap-3 px-6 py-4 rounded-xl items-center w-full cursor-default "
                + (selected ? "bg-[--dark-surface] text-[--on-dark-surface]" : "bg-white text-black")
                // + (!selected && " hover:bg-[--lighter-surface]")
            }>
            <span className={"py-2 px-4 rounded-3xl text-center "
                + (selected
                    ? "bg-[--light-surface] text-[--on-light-surface]"
                    : "bg-[--darker-surface] text-[--on-darker-surface]")}>
                {scenario.name}
            </span>
            <TestDetail name="Score" value={result.score} />
            <TestDetail name="State" value={result.status} />
            <TestDetail name="Run Time" value={result.average_time} />
        </div>
    )
}

function TestDetail({ name, value }: { name: string, value: number | string }) {
    return <div className="flex flex-col items-center text-center">
        <span className="text-md">{name}</span>
        <span className="text-sm">{value}</span>
    </div>
}

export default TestCard;