interface Props {
  progress: number
  message: string
}

export default function ScanProgress({
  progress,
  message,
}: Props) {

  return (
    <div
      className="
        mt-8
        rounded-2xl
        border
        border-slate-800
        bg-[#081121]
        p-6
      "
    >
      <div
        className="
          flex
          items-center
          justify-between
          mb-3
        "
      >
        <p className="font-medium">
          {message}
        </p>

        <p className="text-blue-400">
          {progress}%
        </p>
      </div>

      <div
        className="
          h-4
          overflow-hidden
          rounded-full
          bg-slate-800
        "
      >
        <div
          className="
            h-full
            bg-blue-500
            transition-all
            duration-500
          "
          style={{
            width: `${progress}%`
          }}
        />
      </div>
    </div>
  )
}