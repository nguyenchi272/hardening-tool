import {
  useEffect,
  useState
} from "react"

import {
  getFindings
} from "../../api/dashboard"

import {
  Finding
} from "../../types/finding"

export default function RecentFindings() {

  const [findings, setFindings] =
    useState<Finding[]>([])

  useEffect(() => {

    loadFindings()

  }, [])

  const loadFindings =
    async () => {

      const data =
        await getFindings()

      setFindings(
        data.slice(0, 5)
      )
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

      <h2
        className="
          mb-6
          text-xl
          font-semibold
        "
      >
        Recent Findings
      </h2>

      <div className="space-y-4">

        {findings.map((finding) => (

          <div
            key={finding.id}
            className="
              rounded-xl
              border
              border-slate-700
              bg-slate-900/50
              p-4
            "
          >

            <div
              className="
                flex
                items-center
                justify-between
              "
            >

              <p className="font-medium">
                {finding.title}
              </p>

              <span
                className="
                  text-sm
                  text-red-400
                "
              >
                {finding.severity}
              </span>

            </div>

            <p
              className="
                mt-2
                text-sm
                text-slate-400
              "
            >
              {finding.server}
            </p>

          </div>
        ))}

      </div>

    </div>
  )
}