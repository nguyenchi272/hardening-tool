interface Props {
  title: string
  value: number
  color: string
}

export default function MetricCard({
  title,
  value,
  color,
}: Props) {
  return (
    <div
      className="
        relative
        overflow-hidden
        rounded-2xl
        border
        border-slate-800
        bg-[#081121]
        p-6
        transition-all
        hover:scale-[1.02]
        hover:border-blue-500
      "
    >
      <div
        className={`
          absolute
          inset-0
          opacity-10
          blur-3xl
          ${color}
        `}
      />

      <p className="text-slate-400 text-sm">
        {title}
      </p>

      <h2 className="mt-3 text-5xl font-bold">
        {value}
      </h2>
    </div>
  )
}