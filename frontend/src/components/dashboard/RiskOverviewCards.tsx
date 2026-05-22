import {
  useEffect,
  useState
} from "react"

import {
  getDashboardSummary
} from "../../api/dashboard"

export default function RiskOverviewCards() {

  const [summary, setSummary] =
    useState<any>(null)

  useEffect(() => {

    loadSummary()

  }, [])

  const loadSummary =
    async () => {

      const data =
        await getDashboardSummary()

      setSummary(data)
    }

  if (!summary) {

    return null
  }

  const cards = [

    {
      title: "Assets",
      value: summary.assets
    },

    {
      title: "Findings",
      value: summary.findings
    },

    {
      title: "Critical",
      value: summary.critical
    },

    {
      title: "Risk Score",
      value: summary.risk_score
    }
  ]

  return (

    <div
      className="
        grid
        grid-cols-1
        gap-6
        md:grid-cols-2
        xl:grid-cols-4
      "
    >

      {cards.map((card) => (

        <div
          key={card.title}
          className="
            rounded-2xl
            border
            border-slate-800
            bg-[#081121]
            p-6
          "
        >

          <p
            className="
              text-sm
              text-slate-400
            "
          >
            {card.title}
          </p>

          <h2
            className="
              mt-4
              text-4xl
              font-bold
            "
          >
            {card.value}
          </h2>

        </div>
      ))}

    </div>
  )
}