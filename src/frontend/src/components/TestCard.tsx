function TestCard({ scenario, selected = false }:
    { selected?: boolean, scenario: any }) {
    return (
        <div onClick={() => { }}
            className={"test-card flex justify-between gap-3 px-6 py-4 rounded-xl items-center w-full "
                + (selected ? "bg-[--dark-surface] text-[--on-dark-surface] cursor-default" : "bg-white text-black cursor-pointer")
                + (!selected && " hover:bg-[--lighter-surface]")
            }>
            <span className={"py-2 px-4 rounded-3xl text-center "
                + (selected
                    ? "bg-[--light-surface] text-[--on-light-surface]"
                    : "bg-[--darker-surface] text-[--on-darker-surface]")}>
                {scenario.name}
            </span>
            <TestDetail name="Success Rate" value="90%" />
            <TestDetail name="State" value="pass" />
            <TestDetail name="Run Time" value="3.2 seconds" />
        </div>
    )
}

function TestDetail({ name, value }: { name: string, value: string }) {
    return <div className="flex flex-col items-center text-center">
        <span className="text-md">{name}</span>
        <span className="text-sm">{value}</span>
    </div>
}

export default TestCard;