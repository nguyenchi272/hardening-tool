import {
  useEffect,
  useState
} from "react"

import AppLayout
  from "../components/layout/AppLayout"

import {
  getCompliance
} from "../api/dashboard"

import {
  ComplianceFramework
} from "../types/compliance"

export default function Compliance() {

  const [frameworks, setFrameworks] =
    useState<
      ComplianceFramework[]
    >([])

  useEffect(() => {

    loadCompliance()

  }, [])

  const loadCompliance =
    async () => {

      const data =
        await getCompliance()

      setFrameworks(data)
    }

  const scoreColor = (
    score: number
  ) => {

    if (score >= 85) {

      return `
        text-green-400
      `
    }

    if (score >= 70) {

      return `
        text-yellow-400
      `
    }

    return `
      text-red-400
    `
  }

  const progressColor = (
    score: number
  ) => {

    if (score >= 85) {

      return `
        bg-green-500
      `
    }

    if (score >= 70) {

      return `
        bg-yellow-500
      `
    }

    return `
      bg-red-500
    `
  }

  const statusStyle = (
    status: string
  ) => {

    if (
      status === "Compliant"
    ) {

      return `
        bg-green-500/20
        text-green-400
      `
    }

    return `
      bg-red-500/20
      text-red-400
    `
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
            Compliance
          </h1>

          <p
            className="
              mt-2
              text-slate-400
            "
          >
            Security framework compliance
            overview
          </p>

        </div>

        <div
          className="
            grid
            grid-cols-1
            gap-6
            xl:grid-cols-3
          "
        >

          {frameworks.map((item) => (

            <div
              key={item.framework}
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
                  items-start
                  justify-between
                "
              >

                <div>

                  <p
                    className="
                      text-slate-400
                    "
                  >
                    {item.framework}
                  </p>

                  <h2
                    className={`
                      mt-4
                      text-5xl
                      font-bold
                      ${scoreColor(
                        item.score
                      )}
                    `}
                  >
                    {item.score}%
                  </h2>

                </div>

                <span
                  className={`
                    rounded-full
                    px-3
                    py-1
                    text-sm
                    font-medium
                    ${statusStyle(
                      item.status
                    )}
                  `}
                >
                  {item.status}
                </span>

              </div>

              <div
                className="
                  mt-6
                  h-4
                  overflow-hidden
                  rounded-full
                  bg-slate-800
                "
              >

                <div
                  className={`
                    h-full
                    transition-all
                    duration-700
                    ${progressColor(
                      item.score
                    )}
                  `}
                  style={{
                    width:
                      `${item.score}%`
                  }}
                />

              </div>

              <div
                className="
                  mt-6
                  flex
                  items-center
                  justify-between
                  text-sm
                "
              >

                <span
                  className="
                    text-slate-400
                  "
                >
                  Failed Controls
                </span>

                <span
                  className="
                    font-semibold
                    text-white
                  "
                >
                  {
                    item.failed_controls
                  }
                </span>

              </div>

            </div>
          ))}

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
                  Framework
                </th>

                <th className="p-4 text-left">
                  Score
                </th>

                <th className="p-4 text-left">
                  Failed Controls
                </th>

                <th className="p-4 text-left">
                  Status
                </th>

              </tr>

            </thead>

            <tbody>

              {frameworks.map((item) => (

                <tr
                  key={item.framework}
                  className="
                    border-b
                    border-slate-800
                  "
                >

                  <td className="p-4">
                    {item.framework}
                  </td>

                  <td
                    className={`
                      p-4
                      font-semibold
                      ${scoreColor(
                        item.score
                      )}
                    `}
                  >
                    {item.score}%
                  </td>

                  <td className="p-4">
                    {item.failed_controls}
                  </td>

                  <td className="p-4">

                    <span
                      className={`
                        rounded-full
                        px-3
                        py-1
                        text-sm
                        ${statusStyle(
                          item.status
                        )}
                      `}
                    >
                      {item.status}
                    </span>

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