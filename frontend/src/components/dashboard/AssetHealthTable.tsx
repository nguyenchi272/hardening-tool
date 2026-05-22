import {
  useEffect,
  useState
} from "react"

import {
  getAssets
} from "../../api/dashboard"

export default function AssetHealthTable() {

  const [assets, setAssets] =
    useState<any[]>([])

  useEffect(() => {

    loadAssets()

  }, [])

  const loadAssets =
    async () => {

      const data =
        await getAssets()

      setAssets(data)
    }

  return (

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
              key={asset.hostname}
              className="
                border-b
                border-slate-800
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
                {asset.risk}
              </td>

            </tr>
          ))}

        </tbody>

      </table>

    </div>
  )
}