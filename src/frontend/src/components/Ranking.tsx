import { Team } from "../utils/types"

function suffix(index: number) {
    if (index === 1)
        return "st"
    if (index === 2)
        return "nd"
    if (index === 3)
        return "rd"
    return "th"
}

const bg = "122, 153, 150"
function background(index: number) {
    if (index <= 0)
        throw "Invalid index"
    return `rgba(${bg}, ${(1 / (index ** 1.25))}`
}

function Ranking({ teams }: { teams: Team[] }) {
    return (
        <div className="bg-[--dark-surface] rounded-xl py-3 px-4 flex flex-col gap-2 overflow-scroll flex-1">
            {teams.map((team, index) => {
                return <div key={index} className={
                    "rounded-md flex gap-1 px-4 py-2 items-center " +
                    (index < teams.length / 3 ? "text-[--ranking-winners]" : "text-[--ranking-others]")
                } style={{ backgroundColor: background(index + 1) }}>
                    <span className="relative">
                        <span>{team.rank}</span>
                        <span className="absolute text-[13px] translate-x-[3px] translate-y-[-4px]">{suffix(team.rank)}</span>
                    </span>
                    <span className="text-center flex-1">{team.name}</span>
                </div>
            })}
        </div>
    )
}

export default Ranking