import { useState }
  from "react"

import { Finding }
  from "../types/finding"

interface ScanPayload {
  hosts: string[]
  username: string
  password: string
}

export default function useScanSocket() {

  const [progress, setProgress] =
    useState(0)

  const [message, setMessage] =
    useState("")

  const [findings, setFindings] =
    useState<Finding[]>([])

  const [connected, setConnected] =
    useState(false)

  const [completed, setCompleted] =
    useState(false)

  const [error, setError] =
    useState("")

  const startRealtimeScan =
    (
      payload: ScanPayload
    ) => {

      setProgress(0)

      setMessage("")

      setFindings([])

      setCompleted(false)

      setError("")

      const socket =
        new WebSocket(
          "ws://localhost:8080/api/v1/ws/scan"
        )

      socket.onopen = () => {

        setConnected(true)

        socket.send(
          JSON.stringify(payload)
        )
      }

      socket.onmessage = (event) => {

        const data =
          JSON.parse(event.data)

        console.log(
          "WS EVENT:",
          data
        )

        if (
          data.type === "progress"
        ) {

          setProgress(
            data.progress
          )

          setMessage(
            data.message
          )
        }

        if (
          data.type === "finding"
        ) {

          setFindings((prev) => [
            ...prev,
            data.finding
          ])
        }

        if (
          data.type === "completed"
        ) {

          setCompleted(true)

          socket.close()
        }

        if (
          data.type === "error"
        ) {

          setError(
            data.message
          )

          setCompleted(true)

          socket.close()
        }
      }

      socket.onerror = () => {

        setError(
          "WebSocket connection failed"
        )

        setCompleted(true)

        setConnected(false)
      }

      socket.onclose = () => {

        setConnected(false)

        setCompleted(true)
      }
    }

  return {
    progress,
    message,
    findings,
    connected,
    completed,
    error,
    startRealtimeScan
  }
}