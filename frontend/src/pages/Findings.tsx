import {
  useMemo,
  useState
} from "react"

import AppLayout
  from "../components/layout/AppLayout"

import FindingDrawer
  from "../components/findings/FindingDrawer"

import { Finding }
  from "../types/finding"

import {
  useEffect
} from "react"

import {
  getFindings
} from "../api/dashboard"

export default function Findings() {
  const [findings, setFindings] =
    useState<Finding[]>([])

  useEffect(() => {

    loadFindings()

  }, [])

  const loadFindings =
    async () => {

        const data =
        await getFindings()

        setFindings(data)
  }

  const [search, setSearch] =
    useState("")

  const [severity, setSeverity] =
    useState("All")

  const [
    selectedFinding,
    setSelectedFinding
  ] = useState<Finding | null>(
    null
  )

  const filteredFindings =
    useMemo(() => {

      return findings.filter(
        (finding) => {

          const matchesSearch =
            finding.title
              .toLowerCase()
              .includes(
                search.toLowerCase()
              )

          const matchesSeverity =
            severity === "All"
            || finding.severity === severity

          return (
            matchesSearch
            && matchesSeverity
          )
        }
      )
    }, [findings, search, severity])

  const severityStyle = (
    severity: string
  ) => {

    switch (severity) {

      case "Critical":
        return `
          bg-red-500/20
          text-red-400
        `

      case "High":
        return `
          bg-orange-500/20
          text-orange-400
        `

      case "Medium":
        return `
          bg-yellow-500/20
          text-yellow-400
        `

      default:
        return `
          bg-blue-500/20
          text-blue-400
        `
    }
  }

  return (

    <AppLayout>

      <div className="space-y-8">

        <div>

          <h1
            className="
              text-3xl
              font-bold
            "
          >
            Findings
          </h1>

          <p
            className="
              mt-2
              text-slate-400
            "
          >
            Security vulnerabilities
            across all assets
          </p>

        </div>

        <div
          className="
            flex
            gap-4
          "
        >

          <input
            value={search}
            onChange={(e) =>
              setSearch(
                e.target.value
              )
            }
            placeholder="Search findings..."
            className="
              w-full
              rounded-xl
              border
              border-slate-700
              bg-slate-900
              px-4
              py-3
              outline-none
            "
          />

          <select
            value={severity}
            onChange={(e) =>
              setSeverity(
                e.target.value
              )
            }
            className="
              rounded-xl
              border
              border-slate-700
              bg-slate-900
              px-4
            "
          >

            <option>
              All
            </option>

            <option>
              Critical
            </option>

            <option>
              High
            </option>

            <option>
              Medium
            </option>

            <option>
              Low
            </option>

          </select>

        </div>

        <div
          className="
            overflow-hidden
            rounded-2xl
            border
            border-slate-800
            bg-[#081121]
          "
        >

          <table className="w-full">

            <thead
              className="
                border-b
                border-slate-800
                bg-slate-900/50
              "
            >

              <tr>

                <th className="p-4 text-left">
                  Finding
                </th>

                <th className="p-4 text-left">
                  Severity
                </th>

                <th className="p-4 text-left">
                  Asset
                </th>

                <th className="p-4 text-left">
                  Status
                </th>

              </tr>

            </thead>

            <tbody>

              {filteredFindings.map(
                (finding) => (

                <tr
                  key={finding.id}

                  onClick={() =>
                    setSelectedFinding(
                      finding
                    )
                  }

                  className="
                    cursor-pointer
                    border-b
                    border-slate-800
                    transition-all
                    hover:bg-slate-900/40
                  "
                >

                  <td className="p-4">

                    <div>

                      <p className="font-medium">
                        {finding.title}
                      </p>

                      <p
                        className="
                          mt-1
                          text-xs
                          text-slate-500
                        "
                      >
                        {finding.finding_id}
                      </p>

                    </div>

                  </td>

                  <td className="p-4">

                    <span
                      className={`
                        rounded-full
                        px-3
                        py-1
                        text-sm
                        ${severityStyle(
                          finding.severity
                        )}
                      `}
                    >
                      {finding.severity}
                    </span>

                  </td>

                  <td className="p-4">
                    {finding.server}
                  </td>

                  <td className="p-4">
                    {finding.status}
                  </td>

                </tr>
              ))}

            </tbody>

          </table>

        </div>

      </div>

      {
        selectedFinding && (

          <FindingDrawer
            finding={selectedFinding}
            onClose={() =>
              setSelectedFinding(null)
            }
          />
        )
      }

    </AppLayout>
  )
}