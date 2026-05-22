import {
  useEffect,
  useState
} from "react"

import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
  Legend
} from "recharts"

import {
  getDashboardSummary
} from "../../api/dashboard"

const COLORS = [
  "#ef4444",
  "#f97316",
  "#eab308",
  "#3b82f6"
]

export default function SeverityChart() {

  const [data, setData] =
    useState<any[]>([])

  useEffect(() => {

    loadSummary()

  }, [])

  const loadSummary =
    async () => {

      const summary =
        await getDashboardSummary()

      setData([

        {
          name: "Critical",
          value: summary.critical
        },

        {
          name: "High",
          value: summary.high
        },

        {
          name: "Medium",
          value: summary.medium
        },

        {
          name: "Low",
          value: summary.low
        }
      ])
    }

  return (

    <div
      className="
        rounded-2xl
        border
        border-slate-800
        bg-[#081121]
        p-6
      "
    >

      <div
        className="
          mb-6
          flex
          items-center
          justify-between
        "
      >

        <div>

          <h3
            className="
              text-xl
              font-semibold
            "
          >
            Findings Severity
          </h3>

          <p
            className="
              mt-1
              text-sm
              text-slate-400
            "
          >
            Severity distribution
            across findings
          </p>

        </div>

      </div>

      <div className="h-[320px]">

        <ResponsiveContainer>

          <PieChart>

            <Pie
              data={data}
              dataKey="value"
              nameKey="name"
              outerRadius={120}
              innerRadius={70}
              paddingAngle={4}
            >

              {data.map(
                (_, index) => (

                  <Cell
                    key={index}
                    fill={
                      COLORS[index]
                    }
                  />
                )
              )}

            </Pie>

            <Tooltip />

            <Legend />

          </PieChart>

        </ResponsiveContainer>

      </div>

    </div>
  )
}