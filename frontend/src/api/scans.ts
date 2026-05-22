import api from "./axios"

interface ScanPayload {
  host: string
  username: string
  password: string
}

export const startScan =
  async (payload: ScanPayload) => {
    const response =
      await api.post(
        "/scan",
        payload
      )

    return response.data
  }