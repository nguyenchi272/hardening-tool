import { ReactNode } from "react"

import Sidebar
  from "../layout/Sidebar"

interface Props {
  children: ReactNode
}

export default function AppLayout({
  children
}: Props) {

  return (

    <div
      className="
        flex
        min-h-screen
        bg-[#020817]
        text-white
      "
    >

      <Sidebar />

      <main
        className="
          flex-1
          overflow-y-auto
          p-8
        "
      >

        {children}

      </main>

    </div>
  )
}