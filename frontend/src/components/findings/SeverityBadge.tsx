interface Props {
  severity: string
}

const severityStyles = {
  Critical:
    "bg-red-500/20 text-red-400",

  High:
    "bg-orange-500/20 text-orange-400",

  Medium:
    "bg-yellow-500/20 text-yellow-400",

  Low:
    "bg-blue-500/20 text-blue-400",

  Info:
    "bg-slate-500/20 text-slate-400",
}

export default function SeverityBadge({
  severity,
}: Props) {

  return (
    <span
      className={`
        px-3
        py-1
        rounded-full
        text-sm
        font-medium
        ${
          severityStyles[
            severity as keyof
            typeof severityStyles
          ]
        }
      `}
    >
      {severity}
    </span>
  )
}