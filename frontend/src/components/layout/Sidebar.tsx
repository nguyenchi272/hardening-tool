import {
  Shield,
  LayoutDashboard,
  Server,
  AlertTriangle,
  ScanLine,
  BadgeCheck,
  Key
} from "lucide-react"

import {
  useNavigate,
  useLocation
} from "react-router-dom"

const items = [

  {
    title: "Dashboard",
    path: "/dashboard",
    icon: LayoutDashboard
  },

  {
    title: "Assets",
    path: "/assets",
    icon: Server
  },

  {
    title: "Credentials",
    path: "/credentials",
    icon: Key
  },

  {
    title: "Findings",
    path: "/findings",
    icon: AlertTriangle
  },

  {
    title: "Scans",
    path: "/scans",
    icon: ScanLine
  },

  {
    title: "Compliance",
    path: "/compliance",
    icon: BadgeCheck
  }
]

export default function Sidebar() {

  return (

    <aside
      className="
        flex
        min-h-screen
        w-[260px]
        flex-col
        border-r
        border-slate-800
        bg-[#081121]
      "
    >

      <div
        className="
          flex
          items-center
          gap-3
          border-b
          border-slate-800
          px-6
          py-6
        "
      >

        <div
          className="
            rounded-xl
            bg-blue-600/20
            p-3
          "
        >

          <Shield
            className="
              h-6
              w-6
              text-blue-400
            "
          />

        </div>

        <div>

          <h1
            className="
              text-lg
              font-bold
            "
          >
            SentinelSec
          </h1>

          <p
            className="
              text-xs
              text-slate-500
            "
          >
            Security Platform
          </p>

        </div>

      </div>

      <nav
        className="
          flex-1
          space-y-2
          p-4
        "
      >

        {items.map((item) => {

          const navigate = useNavigate()

          const location = useLocation()
          const Icon = item.icon

          return (

          <button
            key={item.title}

            onClick={() =>
                navigate(item.path)
            }

            className={`
                flex
                w-full
                items-center
                gap-3
                rounded-xl
                px-4
                py-3
                font-medium
                transition-all

                ${
                location.pathname === item.path
                    ? `
                    bg-blue-600/20
                    text-blue-400
                    border
                    border-blue-500/30
                    `
                    : `
                    text-slate-400
                    hover:bg-slate-800
                    hover:text-white
                    `
                }
            `}
            >

            <Icon
                className="
                h-5
                w-5
                shrink-0
                "
            />

            <span>
                {item.title}
            </span>

          </button>
          )
        })}

      </nav>

      <div
        className="
          border-t
          border-slate-800
          p-4
        "
      >

        <div
          className="
            rounded-xl
            bg-slate-900
            p-4
          "
        >

          <p
            className="
              text-sm
              text-slate-400
            "
          >
            Active Assets
          </p>

          <h2
            className="
              mt-2
              text-3xl
              font-bold
            "
          >
            48
          </h2>

        </div>

      </div>

    </aside>
  )
}