import AppLayout
  from "../components/layout/AppLayout"

import ScanForm
  from "../components/scans/ScanForm"

export default function Scan() {
  return (
    <AppLayout>
      <div>
        <h1
          className="
            text-5xl
            font-bold
            mb-3
          "
        >
          Security Scan
        </h1>

        <p className="text-slate-400 mb-10">
          Start Oracle Linux audit scan
        </p>

        <ScanForm />
      </div>
    </AppLayout>
  )
}