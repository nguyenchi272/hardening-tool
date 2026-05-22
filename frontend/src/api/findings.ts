import api from "./axios"

export const getFindings =
  async () => {
    const response =
      await api.get("/findings")

    return response.data
  }