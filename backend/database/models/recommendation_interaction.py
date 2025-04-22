from sqlalchemy import UUID, Column, DateTime, ForeignKey, String, func
from sqlalchemy.orm import relationship
from backend.database import Base


class RecommendationInteraction(Base):
    __tablename__ = "recommendation_interactions"

    id = Column(UUID, primary_key=True, index=True)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="recommendation_interactions")

    recommendation_id = Column(UUID, ForeignKey("recommendations.id"), nullable=False)
    recommendation = relationship("Recommendation", back_populates="interactions")

    interaction_type = Column(String, nullable=False)

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
