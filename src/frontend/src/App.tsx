import Sidebar from './components/Sidebar';
import TestCard from './components/TestCard';
import Steps from './components/Steps';
import Ranking from './components/Ranking';
import { teams, scenarios } from "./utils/data";

const filters = ["website", "core"]

function App() {
  return (
    <div className="main-page flex">
      <Sidebar teams={teams} filters={filters} />
      <main className="flex min-h-screen py-10 px-6 flex-1 gap-4">
        <div className='flex justify-center flex-1'>
          <div className="tests flex flex-col gap-4 w-full max-w-[550px] overflow-y-scroll no-scrollbar">
            <div className='flex items-center gap-2'>
              <span className='text-[--primary] text-lg'>Tests ({scenarios.length})</span>
              <hr className='flex-1 border-white' />
              <button className='py-[6px] px-4 rounded-full bg-[--primary] text-[--on-primary] text-sm'>Run Tests</button>
            </div>
            {
              scenarios.map((scenario, index) => {
                return <TestCard key={index} scenario={scenario} />
              })}
            <hr className='flex-1 border-white' />
          </div>
        </div>
        <div className="details flex flex-col gap-4 w-[300px] bg-[--darker-surface] py-3 px-4 rounded-xl text-[--on-darker-surface]">
          <div className="steps">
            <div className='text-lg mb-2 font-bold'>Steps</div>
            <Steps />
          </div>
          <div className="ranking flex-1 flex flex-col gap-2 overflow-hidden">
            <div className='text-lg font-bold'>Ranking</div>
            <Ranking teams={teams.sort((a, b) => a.rank - b.rank)} />
          </div>
        </div>
      </main>
    </div>
  );
}

export default App