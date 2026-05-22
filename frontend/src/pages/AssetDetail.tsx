import {
  useEffect,
  useState
} from "react"

import {
  useParams
} from "react-router-dom"

import AppLayout
  from "../components/layout/AppLayout"

import {
  getAssetDetail
} from "../api/dashboard"

export default function AssetDetail() {

  const { id } = useParams()

  const [data, setData] =
    useState<any>(null)

  useEffect(() => {

    loadAsset()

  }, [])

  const loadAsset =
    async () => {

      const result =
        await getAssetDetail(
          id || ""
        )

      setData(result)
    }

  if (!data || !data.asset) {

    return (
      <AppLayout>
        Loading...
      </AppLayout>
    )
  }

  return (

    <AppLayout>

      <div className="space-y-8">

        <div 
            className="
                flex
                items-start
                justify-between
            "
        >

          <h1
            className="
              text-3xl
              font-bold
            "
          >
            {data.asset.hostname}
          </h1>

          <p
            className="
              mt-2
              text-slate-400
            "
          >
            {data.asset.ip_address}
          </p>

          <a
            href={
                `http://localhost:8080/api/v1/reports/asset/${id}`
            }
            target="_blank"
            className="
                inline-flex
                items-center
                transition-all
                rounded-xl
                bg-blue-600
                px-5
                py-3
                font-medium
                hover:bg-blue-500
                cursor-pointer
            "
            >
            Export PDF Report
          </a>

        </div>

        <div
          className="
            grid
            grid-cols-1
            gap-6
            md:grid-cols-4
          "
        >

          <div
            className="
              rounded-2xl
              border
              border-slate-800
              bg-[#081121]
              p-6
            "
          >

            <p className="text-slate-400">
              OS
            </p>

            <h2
              className="
                mt-3
                text-xl
                font-bold
              "
            >
              {data.asset.os}
            </h2>

          </div>

          <div
            className="
              rounded-2xl
              border
              border-slate-800
              bg-[#081121]
              p-6
            "
          >

            <p className="text-slate-400">
              Findings
            </p>

            <h2
              className="
                mt-3
                text-4xl
                font-bold
              "
            >
              {data.summary.findings}
            </h2>

          </div>

          <div
            className="
              rounded-2xl
              border
              border-slate-800
              bg-[#081121]
              p-6
            "
          >

            <p className="text-slate-400">
              Risk Score
            </p>

            <h2
              className="
                mt-3
                text-4xl
                font-bold
              "
            >
              {data.summary.risk_score}
            </h2>

          </div>

          <div
            className="
              rounded-2xl
              border
              border-slate-800
              bg-[#081121]
              p-6
            "
          >

            <p className="text-slate-400">
              Status
            </p>

            <h2
              className="
                mt-3
                text-xl
                font-bold
              "
            >
              {data.asset.status}
            </h2>

          </div>

        </div>

        <div
          className="
            rounded-2xl
            border
            border-slate-800
            bg-[#081121]
            overflow-hidden
          "
        >

          <table className="w-full">

            <thead
              className="
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
                  Status
                </th>

              </tr>

            </thead>

            <tbody>

              {data.findings.map(
                (finding: any) => (

                <tr
                  key={finding.id}
                  className="
                    border-t
                    border-slate-800
                  "
                >

                  <td className="p-4">

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

                  </td>

                  <td className="p-4">
                    {finding.severity}
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

    </AppLayout>
  )
}