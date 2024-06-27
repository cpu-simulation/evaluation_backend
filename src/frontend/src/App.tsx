import Sidebar from './components/Sidebar';
import TestCard from './components/TestCard';
import Ranking from './components/Ranking';
import { useEffect, useState } from 'react';
import { Result, Scenario, Team, History } from './utils/types';
import * as lib from './lib';
import HistoryChart from './components/HistoryChart';

function App() {
  const [selectedTeam, setSelectedTeam] = useState<Team>()
  const [teams, setTeams] = useState<Team[]>([])
  const [scenarios, setScenarios] = useState<Scenario[]>([])
  const [history, setHistory] = useState<History>({})
  const [results, setResults] = useState<Result[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState()

  useEffect(() => {
    setLoading(true)
    lib.getTeams()
      .then(teams => {
        setTeams(teams)
        if (teams.length > 0)
          setSelectedTeam(teams[0])
        setLoading(false)
      })
      .catch(e => {
        console.error(e)
        setError(e)
      })

    lib.getScenarios()
      .then(setScenarios)
      .catch(e => {
        console.error(e)
        setError(e)
      })
  }, [])

  const getResult = () => {
    if (selectedTeam) {
      setResults([])
      lib.getResults(selectedTeam).then(setResults).catch(e => {
        console.error(e)
        setError(e)
      })
    }
  }

  const runTests = () => {
    if (selectedTeam)
      lib.runTests(selectedTeam).then(getResult).catch(e => {
        console.error(e)
        setError(e)
      })
  }

  const getHistory = () => {
    if (selectedTeam)
      lib.getHistory(selectedTeam).then(setHistory).catch(e => {
        console.error(e)
        setError(e)
      })
  }

  useEffect(() => {
    getResult()
    getHistory()
  }, [selectedTeam])

  if (error)
    return <div className='h-full w-full flex flex-col gap-2 justify-center items-center'>
      <h1 className='text-center text-2xl'>Unexpected Error !</h1>
      <p>check console for more information or refresh the page</p>
    </div>

  if (loading)
    return <h1 className='text-center mt-8 text-lg'>Loading ...</h1>


  const ranking = [...teams].sort((a, b) => b.total_score - a.total_score)
  return (
    <div className="main-page flex">
      <Sidebar teams={teams} setSelectedTeam={setSelectedTeam} winners={ranking.slice(0, 3)} />
      <main className="flex min-h-screen py-10 px-6 flex-1 gap-4">
        <div className='flex justify-center flex-1'>
          <div className="tests flex flex-col gap-4 w-full max-w-[550px] overflow-y-scroll no-scrollbar">
            <div className='flex items-center gap-2'>
              <span className='text-[--primary] text-lg'>Tests ({scenarios.length})</span>
              <hr className='flex-1 border-white' />
              <button onClick={runTests}
                className='py-[6px] px-4 rounded-full bg-[--primary] text-[--on-primary] text-sm'>
                Run Tests
              </button>
            </div>
            {
              scenarios.map((scenario, index) => {
                const result = results.find(r => r.scenario === scenario.id)
                return <TestCard key={index} scenario={scenario} result={result} />
              })
            }
            <hr className='flex-1 border-white' />
          </div>
        </div>
        <div className="details flex flex-col gap-4 w-[350px] bg-[--darker-surface] py-3 px-4 rounded-xl text-[--on-darker-surface]">
          <div className="steps">
            <div className='text-lg mb-2 font-bold'>History</div>
            <HistoryChart history={history} />
          </div>
          <div className="ranking flex-1 flex flex-col gap-2 overflow-hidden">
            <div className='text-lg font-bold'>Ranking</div>
            <Ranking ranking={ranking} />
          </div>
        </div>
      </main>
    </div>
  );
}

export default App