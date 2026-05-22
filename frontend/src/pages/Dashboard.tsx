import RiskOverviewCards
  from "../components/dashboard/RiskOverviewCards"

import SeverityChart
  from "../components/dashboard/SeverityChart"

import RecentFindings
  from "../components/dashboard/RecentFindings"

import AssetHealthTable
  from "../components/dashboard/AssetHealthTable"

import AppLayout
  from "../components/layout/AppLayout"

export default function Dashboard() {

  return (
    <AppLayout>
    <div className="space-y-8">

      <RiskOverviewCards />

      <div
        className="
          grid
          grid-cols-1
          gap-6
          xl:grid-cols-2
        "
      >

        <SeverityChart />

        <RecentFindings />

      </div>

      <AssetHealthTable />

    </div>
    </AppLayout>
  )
}