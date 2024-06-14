import { useEffect, useState } from "react"
import profile from "../utils/icons/profile.svg"
import crown from "../utils/icons/crown.svg"
import { Team } from "../utils/types"

function Sidebar({ teams, winners, filters, setSelectedTeam }:
    { teams: Team[], winners: Team[], filters: string[], setSelectedTeam: Function }) {
    const [selectedFilter, _setSelectedFilter] = useState(filters[0])
    const [selectedIndex, setSelectedIndex] = useState(0)
    const teamsList = teams.filter(team => team.type === selectedFilter)

    useEffect(() => {
        setSelectedTeam(teamsList[selectedIndex])
    }, [selectedIndex, selectedFilter])


    function setSelectedFilter(filter: string) {
        _setSelectedFilter(filter)
        setSelectedIndex(0)
    }

    return (
        <div className="sidebar w-[240px] rounded-r-2xl flex flex-col">
            <div className="header flex flex-col items-center justify-center bg-[--darker-surface] px-2 py-6 gap-6">
                <div className="flex tab-switcher bg-[--dark-surface] p-1 rounded-full">
                    {filters.map((filter, index) => {
                        if (filter === selectedFilter)
                            return <span key={index} className="px-5 cursor-default py-1 bg-[--light-surface] rounded-full">
                                {filter}
                            </span>
                        else
                            return <span key={index} className="px-5 py-1 cursor-pointer rounded-full text-[--on-dark-surface]"
                                onClick={() => { setSelectedFilter(filters[index]) }}>{filter}</span>
                    })}
                </div>
                <div className="profile">
                    <img src={profile} alt='profile' width={72} height={72} />
                    {teamsList.length > 0
                        ? <div className='text-[--on-darker-surface] mt-1'>{teamsList[selectedIndex].name}</div>
                        : <div className='text-[--on-darker-surface] mt-1'>No Team</div>
                    }
                </div>
            </div>
            <div className="teams-list overflow-y-scroll">
                {
                    teamsList.length > 0
                        ? <>
                            <div className="top bg-[--dark-surface] flex flex-col rounded-br-xl pb-2">
                                {teamsList.slice(0, selectedIndex).map((team, index) => {
                                    return <TeamItem key={index} name={team.name} onClick={() => { setSelectedIndex(index) }} />
                                })}
                            </div>
                            <div className="selected bg-[--dark-surface]">
                                <TeamItem name={teamsList[selectedIndex].name} selected={true} />
                            </div>
                            <div className="bottom flex flex-col rounded-tr-xl bg-[--dark-surface] pt-2">
                                {teamsList.slice(selectedIndex + 1).map((team, index) => {
                                    return <TeamItem name={team.name} key={index}
                                        onClick={() => { setSelectedIndex(selectedIndex + index + 1) }} />
                                })}
                            </div>
                        </>
                        : <div className="bg-[--dark-surface] text-[--on-dark-surface] p-4 text-lg">
                            There is no team in this category
                        </div>
                }
            </div>
            <div className='spcae flex-1 bg-[--dark-surface]'></div>
            <div className='bg-[--darker-surface] px-2 py-8 flex gap-2 items-center justify-around 
                            text-[--on-darker-surface] text-sm text-center'>
                {winners.length >= 3 && <WinnerAvatar name={winners[2].name} rank={3} />}
                {winners.length >= 1 && <WinnerAvatar name={winners[0].name} rank={1} />}
                {winners.length >= 2 && <WinnerAvatar name={winners[1].name} rank={2} />}
            </div>
        </div>
    )
}

const avatar = {
    border: {
        1: "#D7A30F",
        2: "#C56B2A",
        3: "#D9D9D9",
        0: "#D9D9D9"
    },
    className: {
        1: "winner",
        2: "second",
        3: "third",
        0: "third"
    },
    size: {
        1: 72,
        0: 48
    },
    cSize: {
        1: 28,
        0: 24
    },
    font: {
        1: "13px",
        0: "12px"
    }
}


function getDetail(obj: any, key: number) {
    return obj[key] || obj[0]
}

function WinnerAvatar({ name, rank }:
    { name: string, rank: number }) {
    return <div className={`flex flex-col justify-center items-center ${getDetail(avatar.className, rank)}`}>
        <span className='z-10 mb-[-6px] relative flex items-center justify-center'>
            <img src={crown} alt="" width={getDetail(avatar.cSize, rank)} height={getDetail(avatar.cSize, rank)} />
            <span className={`absolute top-1 text-[${getDetail(avatar.font, rank)}] font-bold text-black`}>{rank}</span>
        </span>
        <div className="container bg-[#D9D9D9] rounded-full p-[2px]">
            <img src={profile} alt="" width={getDetail(avatar.size, rank)} height={getDetail(avatar.size, rank)} />
        </div>
        <div>{name}</div>
    </div>
}

function TeamItem({ name = "Team Name", onClick = () => { }, selected = false }:
    { name?: string, onClick?: Function, selected?: boolean }) {
    return (
        <div className={selected ? 'pl-4 cursor-default' : 'pl-4 py-2 cursor-pointer'} onClick={() => { onClick() }}>
            <div className={"team-item rounded-l-full p-2 flex gap-2 items-center "
                + (selected ? "bg-[--light-surface] text-black" : "text-[--on-dark-surface]")}>
                <img className={'border rounded-full ' + (selected ? "border-[--darker-surface]" : "border-white")}
                    src={profile} alt="profile" width={32} height={32} />
                <span>{name}</span>
            </div>
        </div>
    )
}

export default Sidebar