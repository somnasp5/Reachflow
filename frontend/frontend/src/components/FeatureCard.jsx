function FeatureCard({ title, description }) {
  return (
    <div className="bg-white p-8 rounded-3xl shadow-sm border border-gray-100 hover:shadow-md transition">
      <h2 className="text-2xl font-semibold text-gray-900">
        {title}
      </h2>

      <p className="mt-4 text-gray-600 leading-7">
        {description}
      </p>
    </div>
  );
}

export default FeatureCard;