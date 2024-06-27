import Chart from "chart.js/auto"
import { useEffect, useRef } from "react"

Chart.defaults.color = "#fee"

const HistoryChart = ({ history }: { history: any }) => {
    const chartRef = useRef(null)
    useEffect(() => {
        if (!chartRef.current)
            return
        const chart = new Chart(chartRef.current, {
            type: "line",
            options: {
                color: "#fff",
                plugins: {
                    legend: {
                        display: false
                    },
                },
                scales: {
                    y: {
                        beginAtZero: true,
                    }
                }
            },
            data: {
                labels: Object.keys(history),
                datasets: [
                    {
                        label: "score",
                        data: Object.values(history),
                        tension: 0.4,
                        fill: true,
                        borderColor: "#69ff15",
                        backgroundColor: "#69ff1520"
                    }
                ]
            }
        })
        return () => {
            chart.destroy()
        }
    }, [history])
    return <div className="bg-[--dark-surface] rounded-xl py-3 px-4 flex-1">
        <canvas ref={chartRef} height={200} id="history-line-chart"></canvas>
    </div>
}
export default HistoryChart