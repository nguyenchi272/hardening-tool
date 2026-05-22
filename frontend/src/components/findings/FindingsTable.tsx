import { useEffect, useState }
  from "react"

import { getFindings }
  from "../../api/findings"

import SeverityBadge
  from "./SeverityBadge"

import { Finding }
  from "../../types/finding"

export default function FindingsTable() {

  const [findings, setFindings] =
    useState<Finding[]>([])

  useEffect(() => {
    loadFindings()
  }, [])

  const loadFindings = async () => {
    const data =
      await getFindings()

    setFindings(data)
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
          flex
          items-center
          justify-between
          mb-6
        "
      >
        <h2
          className="
            text-2xl
            font-semibold
          "
        >
          Recent Findings
        </h2>

        <button
          className="
            rounded-xl
            bg-slate-800
            px-4
            py-2
            text-sm
            hover:bg-slate-700
          "
        >
          Export
        </button>
      </div>

      <div className="overflow-auto">

        <table className="w-full">

          <thead>

            <tr
              className="
                text-slate-400
                border-b
                border-slate-800
              "
            >
              <th className="text-left pb-4">
                Severity
              </th>

              <th className="text-left pb-4">
                Finding
              </th>

              <th className="text-left pb-4">
                Category
              </th>

              <th className="text-left pb-4">
                Risk
              </th>

              <th className="text-left pb-4">
                Server
              </th>

            </tr>

          </thead>

          <tbody>

            {findings.map((finding) => (

              <tr
                key={finding.id}
                className="
                  border-b
                  border-slate-900
                  hover:bg-slate-900/40
                  transition-all
                "
              >
                <td className="py-5">
                  <SeverityBadge
                    severity={
                      finding.severity
                    }
                  />
                </td>

                <td className="py-5">
                  <div>
                    <p
                      className="
                        font-semibold
                      "
                    >
                      {finding.title}
                    </p>

                    <p
                      className="
                        text-sm
                        text-slate-400
                        mt-1
                      "
                    >
                      {
                        finding
                          .finding_id
                      }
                    </p>
                  </div>
                </td>

                <td className="py-5">
                  {finding.category}
                </td>

                <td className="py-5">
                  <span
                    className="
                      font-bold
                    "
                  >
                    {
                      finding
                        .risk_score
                    }
                  </span>
                </td>

                <td className="py-5">
                  {finding.server}
                </td>

              </tr>
            ))}

          </tbody>
        </table>
      </div>
    </div>
  )
}