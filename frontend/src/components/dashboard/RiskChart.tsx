import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
} from "recharts"

const data = [
  { name: "Critical", value: 5 },
  { name: "High", value: 12 },
  { name: "Medium", value: 28 },
  { name: "Low", value: 46 },
]

const COLORS = [
  "#ef4444",
  "#f97316",
  "#eab308",
  "#3b82f6",
]

export default function RiskChart() {
  return (
    <ResponsiveContainer
      width="100%"
      height={300}
    >
      <PieChart>
        <Pie
          data={data}
          innerRadius={80}
          outerRadius={120}
          dataKey="value"
        >
          {data.map((_, index) => (
            <Cell
              key={index}
              fill={COLORS[index]}
            />
          ))}
        </Pie>
      </PieChart>
    </ResponsiveContainer>
  )
}