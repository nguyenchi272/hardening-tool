import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom"

import Dashboard
  from "./pages/Dashboard"

import Assets
  from "./pages/Assets"

import Findings
  from "./pages/Findings"

import Scans
  from "./pages/Scan"

import Compliance
  from "./pages/Compliance"

import AssetDetail
  from "./pages/AssetDetail"

import Credentials from "./pages/Credentials"

export default function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={
            <Navigate to="/dashboard" />
          }
        />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/assets"
          element={<Assets />}
        />

        <Route
          path="/findings"
          element={<Findings />}
        />

        <Route
          path="/scans"
          element={<Scans />}
        />

        <Route
          path="/compliance"
          element={<Compliance />}
        />

        <Route
          path="/assets/:id"
          element={<AssetDetail />}
        />

        <Route
          path="/credentials"
          element={<Credentials />}
        />

      </Routes>

    </BrowserRouter>
  )
}