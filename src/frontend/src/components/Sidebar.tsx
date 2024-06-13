import { useState } from "react"
import profile from "../utils/icons/profile.svg"
import crown from "../utils/icons/crown.svg"
import { Team } from "../utils/types"

function Sidebar({ teams, filters }: { teams: Team[], filters: string[] }) {
    const [selectedFilter, _setSelectedFilter] = useState(filters[0])
    const [teamsList, setTeamsList] = useState(teams.filter(team => team.type === selectedFilter))
    const [selectedIndex, setSelectedIndex] = useState(0)

    function setSelectedFilter(filter: string) {
        console.log(filter)
        _setSelectedFilter(filter)
        const t = teams.filter(team => team.type === filter)
        setTeamsList(t)
        setSelectedIndex(0)
    }
    return (
        <div className="sidebar w-[240px] rounded-r-2xl flex flex-col">
            <div className="header flex flex-col items-center justify-center bg-[--darker-surface] px-2 py-6 gap-6">
                <div className="flex tab-switcher bg-[--dark-surface] p-1 rounded-full">
                    {filters.map((filter, index) => {
                        if (filter === selectedFilter)
                            return <span key={index} className="px-5 cursor-default py-1 bg-[--light-surface] rounded-full">{filter}</span>
                        else
                            return <span key={index} className="px-5 py-1 cursor-pointer rounded-full text-[--on-dark-surface]"
                                onClick={() => { setSelectedFilter(filters[index]) }}>{filter}</span>
                    })}
                </div>
                <div className="profile">
                    <img src={profile} alt='profile' width={72} height={72} />
                    <div className='text-[--on-darker-surface] mt-1'>{teamsList[selectedIndex].name}</div>
                </div>
            </div>
            <div className="teams-list overflow-y-scroll">
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
                        return <TeamItem name={team.name} key={index} onClick={() => { setSelectedIndex(selectedIndex + index + 1) }} />
                    })}
                </div>
            </div>
            <div className='spcae flex-1 bg-[--dark-surface]'></div>
            <div className='bg-[--darker-surface] px-2 py-8 flex gap-2 items-center justify-around text-[--on-darker-surface] text-sm text-center'>
                <div className="third flex flex-col justify-center items-center">
                    <span className='z-10 mb-[-6px] relative flex items-center justify-center'>
                        <img src={crown} alt="" width={24} height={24} />
                        <span className="absolute top-1 text-[12px] font-bold text-black">3</span>
                    </span>
                    <div className="container bg-[#D9D9D9] rounded-full p-[2px]">
                        <img src={profile} alt="" width={48} height={48} />
                    </div>
                    <div>Team C</div>
                </div>
                <div className="winner flex flex-col justify-center items-center">
                    <span className='z-10 mb-[-6px] relative flex items-center justify-center'>
                        <img src={crown} alt="" width={28} height={28} />
                        <span className="absolute top-1 text-[13px] font-bold text-black">1</span>
                    </span>
                    <div className="container bg-[#D7A30F] rounded-full p-[2px]">
                        <img src={profile} alt="" width={72} height={72} />
                    </div>
                    <div>Team A</div>
                </div>
                <div className="second flex flex-col justify-center items-center">
                    <span className='z-10 mb-[-6px] relative flex items-center justify-center'>
                        <img src={crown} alt="" width={24} height={24} />
                        <span className="absolute top-1 text-[12px] font-bold text-black">2</span>
                    </span>
                    <div className="container bg-[#C56B2A] rounded-full p-[2px]">
                        <img src={profile} alt="" width={48} height={48} />
                    </div>
                    <div>Team B</div>
                </div>
            </div>
        </div>
    )
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