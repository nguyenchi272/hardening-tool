import {
  useEffect,
  useState
} from "react"

import FindingDrawer
  from "../findings/FindingDrawer"

import { Finding }
  from "../../types/finding"

import useScanSocket
  from "../../hooks/useScanSocket"

import ScanProgress
  from "./ScanProgress"

export default function ScanForm() {

  const [targets, setTargets] =
    useState("")

  const [scanning, setScanning] =
    useState(false)

  const [credentials, setCredentials] =
    useState<any[]>([])

  const [credentialId, setCredentialId] =
    useState<number | null>(null)

  const [
    selectedFinding,
    setSelectedFinding
  ] = useState<Finding | null>(
    null
  )

  const {
    progress,
    message,
    findings,
    completed,
    error,
    startRealtimeScan
  } = useScanSocket()

  useEffect(() => {

    fetch(
      "http://localhost:8080/api/v1/credentials"
    )
      .then((res) => res.json())
      .then((data) => {

        setCredentials(data)

        if (data.length > 0) {

          setCredentialId(
            data[0].id
          )
        }
      })

  }, [])

  useEffect(() => {

    if (completed) {

      setScanning(false)
    }

  }, [completed])

  const handleScan = async () => {
    const hosts =
        targets
            .split("\n")
            .map((h) => h.trim())
            .filter(Boolean)

        setScanning(true)
    
    startRealtimeScan({
      hosts,
      credential_id: Number(credentialId)
    })
  }

  const getSeverityStyle = (
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

      case "Low":
        return `
          bg-blue-500/20
          text-blue-400
        `

      default:
        return `
          bg-slate-500/20
          text-slate-400
        `
    }
  }

  return (

    <div
      className="
        max-w-2xl
        rounded-2xl
        border
        border-slate-800
        bg-[#081121]
        p-8
      "
    > 

      <h2
      className="
        text-3xl
        font-bold
        mb-8
      "
      >
      Start Security Scan
      </h2>

      

      <div>

        <label
          className="
            mb-2
            block
            text-sm
            text-slate-400
          "
        >
          Saved Credential
        </label>

        <select
          value={credentialId ?? ""}
          onChange={(e) =>
            setCredentialId(
              Number(e.target.value)
            )
          }
          className="
            w-full
            rounded-xl
            border
            border-slate-700
            bg-slate-900
            px-4
            py-3
          "
        >
          <option value="">
            Select Credential
          </option>
          {credentials.map((cred) => (

            <option
              key={cred.id}
              value={cred.id}
            >
              {cred.name}
              {" • "}
              {cred.username}
            </option>
          ))}

        </select>

      </div>
      

      <div className="space-y-6">
        <div>

          <label
            className="
              text-sm
              text-slate-400
            "
          >
            Server IP / Hostname
          </label>

          <textarea
            value={targets}

            onChange={(e) =>
              setTargets(
                e.target.value
              )
            }

            placeholder={`
              172.22.1.10
              172.22.1.11
              server01.local
            `}

            className="
              mt-2
              min-h-[160px]
              w-full
              rounded-xl
              border
              border-slate-700
              bg-slate-900
              px-4
              py-3
              font-mono
              outline-none
              focus:border-blue-500
            "
          />

          <p
            className="
              mt-2
              text-xs
              text-slate-500
            "
          >
            One target per line
          </p>

        </div>

        <button
          onClick={handleScan}
          disabled={
            scanning ||
            !targets ||
            !credentialId
          }
          className="
            w-full
            rounded-xl
            bg-blue-600
            py-4
            font-semibold
            transition-all
            hover:bg-blue-500
            disabled:cursor-not-allowed
            disabled:opacity-50
          "
        >
          {
            scanning
              ? "Scanning..."
              : "Start Scan"
          }
        </button>

        {
          scanning && (
            <ScanProgress
              progress={progress}
              message={message}
            />
          )
        }

        {
          findings.length > 0 && (

            <div
              className="
                mt-6
                rounded-2xl
                border
                border-slate-800
                bg-[#081121]
                p-6
              "
            >

              <h3
                className="
                  text-xl
                  font-semibold
                  mb-4
                "
              >
                Live Findings
              </h3>

              <div className="space-y-4">

                {findings.map((finding, index) => (

                  <div
                    key={`${finding.finding_id}-${index}`}
                      onClick={() =>
                      setSelectedFinding(
                      finding
                      )
                    }
                    className="
                      rounded-xl
                      border
                      border-slate-700
                      bg-slate-900/50
                      p-4
                      transition-all
                      hover:border-slate-600
                      cursor-pointer
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

                        <p className="font-semibold">
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

                      <span
                        className={`
                          rounded-full
                          px-3
                          py-1
                          text-sm
                          font-medium
                          ${getSeverityStyle(
                            finding.severity
                          )}
                        `}
                      >
                        {finding.severity}
                      </span>

                    </div>

                    <p
                      className="
                        mt-3
                        text-sm
                        text-slate-400
                      "
                    >
                      {finding.evidence}
                    </p>

                  </div>
                ))}

              </div>

            </div>
          )
        }

        {
          error && (

            <div
              className="
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
          completed && (

            <div
              className="
                rounded-xl
                border
                border-green-500/30
                bg-green-500/10
                p-5
              "
            >

              <p
                className="
                  text-lg
                  font-semibold
                  text-green-400
                "
              >
                Scan Completed
              </p>

              <div
                className="
                  mt-4
                  space-y-2
                  text-sm
                  text-slate-300
                "
              >

                <p>
                    <span className="text-slate-400">
                        Targets:
                    </span>
                    {" "}
                    {
                        targets
                        .split("\n")
                        .filter(Boolean)
                        .length
                    }
                </p>

                <p>
                  <span className="text-slate-400">
                    Findings:
                  </span>
                  {" "}
                  {findings.length}
                </p>

                <p>
                  <span className="text-slate-400">
                    Status:
                  </span>
                  {" "}
                  Completed
                </p>

              </div>

            </div>
          )
        }

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
    </div>
  )
}