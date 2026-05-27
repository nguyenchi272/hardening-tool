import {
  useState
} from "react"

interface Props {

  open: boolean

  assetId: number

  findingId: string

  onClose: () => void
}

export default function FixModal({

  open,

  assetId,

  findingId,

  onClose

}: Props) {

  const [loading, setLoading] =
    useState(false)

  const [result, setResult] =
    useState<any>(null)

  const [error, setError] =
    useState("")

  if (!open) {

    return null
  }

  const handleFix =
    async () => {

      try {

        setLoading(true)

        setError("")

        const response =
          await fetch(
            "http://localhost:8080/api/v1/fix",
            {
              method: "POST",

              headers: {
                "Content-Type":
                  "application/json"
              },

              body: JSON.stringify({

                asset_id:
                  assetId,

                finding_id:
                  findingId
              })
            }
          )

        const data =
          await response.json()

        if (!response.ok) {

          throw new Error(
            data.detail ||
            "Fix failed"
          )
        }

        setResult(data)

      } catch (err: any) {

        setError(err.message)

      } finally {

        setLoading(false)
      }
    }

  return (

    <div
      className="
        fixed
        inset-0
        z-50
        flex
        items-center
        justify-center
        bg-black/70
      "
    >

      <div
        className="
          w-full
          max-w-xl
          rounded-2xl
          border
          border-slate-700
          bg-[#081121]
          p-8
        "
      >

        <div
          className="
            flex
            items-center
            justify-between
          "
        >

          <div>

            <h2
              className="
                text-2xl
                font-bold
              "
            >
              Auto Remediation
            </h2>

            <p
              className="
                mt-2
                text-sm
                text-slate-400
              "
            >
              {findingId}
            </p>

          </div>

          <button
            onClick={onClose}
            className="
              text-slate-400
              hover:text-white
            "
          >
            ✕
          </button>

        </div>

        <div className="mt-6">

          <div
            className="
              rounded-xl
              border
              border-blue-500/30
              bg-blue-500/10
              p-4
              text-sm
              text-blue-300
            "
          >
            Credential will be loaded
            automatically from asset.
          </div>

          <button
            onClick={handleFix}
            disabled={loading}
            className="
              mt-6
              w-full
              rounded-xl
              bg-blue-600
              py-4
              font-semibold
              hover:bg-blue-500
              disabled:opacity-50
            "
          >
            {
              loading
                ? "Running Fix..."
                : "Run Auto Fix"
            }
          </button>

          {
            error && (

              <div
                className="
                  mt-4
                  rounded-xl
                  border
                  border-red-500/30
                  bg-red-500/10
                  p-4
                  text-red-400
                "
              >
                {error}
              </div>
            )
          }

          {
            result && (

              <div
                className="
                  mt-6
                  rounded-xl
                  border
                  border-green-500/30
                  bg-green-500/10
                  p-4
                "
              >

                <p
                  className="
                    mb-4
                    font-semibold
                    text-green-400
                  "
                >
                  Remediation Completed
                </p>

                <div className="space-y-4">

                  {result?.results?.map(
                    (
                      item: any,
                      index: number
                    ) => (

                      <div
                        key={index}
                        className="
                          rounded-lg
                          bg-slate-950
                          p-4
                          font-mono
                          text-sm
                        "
                      >

                        <p
                          className="
                            text-blue-400
                          "
                        >
                          $
                          {" "}
                          {item.command}
                        </p>

                        {
                          item.stdout && (

                            <pre
                              className="
                                mt-3
                                whitespace-pre-wrap
                                text-green-400
                              "
                            >
                              {item.stdout}
                            </pre>
                          )
                        }

                        {
                          item.stderr && (

                            <pre
                              className="
                                mt-3
                                whitespace-pre-wrap
                                text-red-400
                              "
                            >
                              {item.stderr}
                            </pre>
                          )
                        }

                      </div>
                    )
                  )}

                </div>

              </div>
            )
          }

        </div>

      </div>

    </div>
  )
}