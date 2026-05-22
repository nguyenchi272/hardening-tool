import api from "./axios"

export const getFindings =
  async () => {

    const response =
      await api.get(
        "/dashboard/findings"
      )

    return response.data
}

export const getAssets =
  async () => {

    const response =
      await api.get(
        "/dashboard/assets"
      )

    return response.data
}

export const getCompliance =
  async () => {

    const response =
      await api.get(
        "/dashboard/compliance"
      )

    return response.data
}

export const getDashboardSummary =
  async () => {

    const response =
      await api.get(
        "/dashboard/summary"
      )

    return response.data
}

export async function getAssetDetail(
  assetId: string
) {

  const response =
    await fetch(
      `http://localhost:8080/api/v1/assets/${assetId}`
    )

  return response.json()
}