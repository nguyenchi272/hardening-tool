import AppLayout
  from "../components/layout/AppLayout"
import {
  useEffect,
  useState
} from "react"

import {
  getAssets
} from "../api/dashboard"

import { Asset } from "../types/asset"

import {
  useNavigate
} from "react-router-dom"

export default function Assets() {
  const [assets, setAssets] =
    useState<Asset[]>([])

  useEffect(() => {

    loadAssets()

  }, [])

  const loadAssets =
  async () => {

    const data =
      await getAssets()

    setAssets(data)
  }

  const navigate = useNavigate()

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
            Assets
          </h1>

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
              "
            >

              <tr>

                <th className="p-4 text-left">
                  Hostname
                </th>

                <th className="p-4 text-left">
                  OS
                </th>

                <th className="p-4 text-left">
                  Findings
                </th>

                <th className="p-4 text-left">
                  Risk
                </th>

              </tr>

            </thead>

            <tbody>

              {assets.map((asset) => (

                <tr
                  key={asset.id}

                  onClick={() =>
                    navigate(
                      `/assets/${asset.id}`
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
                    {asset.hostname}
                  </td>

                  <td className="p-4">
                    {asset.os}
                  </td>

                  <td className="p-4">
                    {asset.findings}
                  </td>

                  <td className="p-4">

                    <span
                      className="
                        rounded-full
                        bg-red-500/20
                        px-3
                        py-1
                        text-red-400
                      "
                    >
                      {asset.risk}
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