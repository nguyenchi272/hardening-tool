import {
  useEffect,
  useState
} from "react"

import AppLayout
  from "../components/layout/AppLayout"

interface Credential {

  id: number

  name: string

  username: string

  sudo_enabled: boolean
}

export default function Credentials() {

  const [credentials, setCredentials] =
    useState<Credential[]>([])

  const [name, setName] =
    useState("")

  const [username, setUsername] =
    useState("")

  const [password, setPassword] =
    useState("")

  const [sudoEnabled, setSudoEnabled] =
    useState(false)

  const [loading, setLoading] =
    useState(false)

  useEffect(() => {

    loadCredentials()

  }, [])

  const loadCredentials =
    async () => {

      const response =
        await fetch(
          "http://localhost:8080/api/v1/credentials"
        )

      const data =
        await response.json()

      setCredentials(data)
    }

  const createCredential =
    async () => {

      try {

        setLoading(true)

        await fetch(
          "http://localhost:8080/api/v1/credentials",
          {
            method: "POST",

            headers: {
              "Content-Type":
                "application/json"
            },

            body: JSON.stringify({

              name,

              username,

              password,

              sudo_enabled:
                sudoEnabled
            })
          }
        )

        setName("")
        setUsername("")
        setPassword("")
        setSudoEnabled(false)

        loadCredentials()

      } finally {

        setLoading(false)
      }
    }

  const deleteCredential =
    async (
      credentialId: number
    ) => {

      await fetch(
        `http://localhost:8080/api/v1/credentials/${credentialId}`,
        {
          method: "DELETE"
        }
      )

      loadCredentials()
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
            Credentials
          </h1>

          <p
            className="
              mt-2
              text-slate-400
            "
          >
            Manage saved SSH credentials
          </p>

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

          <h2
            className="
              mb-6
              text-xl
              font-semibold
            "
          >
            Add Credential
          </h2>

          <div
            className="
              grid
              gap-4
              md:grid-cols-2
            "
          >

            <input
              placeholder="Credential Name"
              value={name}
              onChange={(e) =>
                setName(
                  e.target.value
                )
              }
              className="
                rounded-xl
                border
                border-slate-700
                bg-slate-900
                px-4
                py-3
              "
            />

            <input
              placeholder="SSH Username"
              value={username}
              onChange={(e) =>
                setUsername(
                  e.target.value
                )
              }
              className="
                rounded-xl
                border
                border-slate-700
                bg-slate-900
                px-4
                py-3
              "
            />

            <input
              type="password"
              placeholder="SSH Password"
              value={password}
              onChange={(e) =>
                setPassword(
                  e.target.value
                )
              }
              className="
                rounded-xl
                border
                border-slate-700
                bg-slate-900
                px-4
                py-3
              "
            />

            <label
              className="
                flex
                items-center
                gap-3
                rounded-xl
                border
                border-slate-700
                bg-slate-900
                px-4
                py-3
              "
            >

              <input
                type="checkbox"
                checked={sudoEnabled}
                onChange={(e) =>
                  setSudoEnabled(
                    e.target.checked
                  )
                }
              />

              Sudo Enabled

            </label>

          </div>

          <button
            onClick={createCredential}
            disabled={loading}
            className="
              mt-6
              rounded-xl
              bg-blue-600
              px-6
              py-3
              font-semibold
              hover:bg-blue-500
              disabled:opacity-50
            "
          >
            {
              loading
                ? "Saving..."
                : "Save Credential"
            }
          </button>

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
                  Name
                </th>

                <th className="p-4 text-left">
                  Username
                </th>

                <th className="p-4 text-left">
                  Sudo
                </th>

                <th className="p-4 text-left">
                  Actions
                </th>

              </tr>

            </thead>

            <tbody>

              {credentials.map((c) => (

                <tr
                  key={c.id}
                  className="
                    border-b
                    border-slate-800
                  "
                >

                  <td className="p-4">
                    {c.name}
                  </td>

                  <td className="p-4">
                    {c.username}
                  </td>

                  <td className="p-4">

                    {
                      c.sudo_enabled
                        ? "Yes"
                        : "No"
                    }

                  </td>

                  <td className="p-4">

                    <button
                      onClick={() =>
                        deleteCredential(
                          c.id
                        )
                      }
                      className="
                        rounded-lg
                        bg-red-500/20
                        px-4
                        py-2
                        text-red-400
                        hover:bg-red-500/30
                      "
                    >
                      Delete
                    </button>

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