from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field

class MarketStrategy(BaseModel):
    """Market strategy model"""
    name: str = Field(..., description="Name of the market strategy")
    tactics: List[str] = Field(..., description="List of tactics to be used in the market strategy")
    channels: List[str] = Field(..., description="List of channels to be used in the market strategy")
    KPIs: List[str] = Field(..., description="List of KPIs to be used in the market strategy")

class CampaignIdea(BaseModel):
    """Campaign idea model"""
    name: str = Field(..., description="Name of the campaign idea")
    description: str = Field(..., description="Description of the campaign idea")
    audience: str = Field(..., description="Audience of the campaign idea")
    channel: str = Field(..., description="Channel of the campaign idea")

class Copy(BaseModel):
    """Copy model"""
    title: str = Field(..., description="Title of the copy")
    body: str = Field(..., description="Body of the copy")

@CrewBase
class MarketingPostsCrew:
    """MarketingPosts crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    shared_memory = {}  # Shared memory for agent communication

    @agent
    def business_information_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['business_information_extractor'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            memory=True,
            shared_memory=self.shared_memory
        )

    @agent
    def audience_demographic_mapper(self) -> Agent:
        return Agent(
            config=self.agents_config['audience_demographic_mapper'],
            tools=[SerperDevTool()],
            verbose=True,
            memory=True,
            shared_memory=self.shared_memory
        )

    @agent
    def market_research_fact_collector(self) -> Agent:
        return Agent(
            config=self.agents_config['market_research_fact_collector'],
            tools=[SerperDevTool()],
            verbose=True,
            memory=True,
            shared_memory=self.shared_memory
        )

    @agent
    def competitor_snapshot_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['competitor_snapshot_agent'],
            tools=[SerperDevTool()],
            verbose=True,
            memory=True,
            shared_memory=self.shared_memory
        )

    @agent
    def brand_essence_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['brand_essence_extractor'],
            verbose=True,
            memory=True,
            shared_memory=self.shared_memory
        )

    @agent
    def chief_marketing_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_marketing_strategist'],
            tools=[SerperDevTool()],
            verbose=True,
            memory=True,
            shared_memory=self.shared_memory
        )

    @agent
    def creative_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_content_creator'],
            verbose=True,
            memory=True,
            shared_memory=self.shared_memory
        )

    @agent
    def ad_copy_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['ad_copy_specialist'],
            verbose=True,
            memory=True,
            shared_memory=self.shared_memory
        )

    @agent
    def design_review_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['design_review_agent'],
            verbose=True,
            memory=True,
            shared_memory=self.shared_memory
        )

    @agent
    def strategic_feedback_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['strategic_feedback_coordinator'],
            verbose=True,
            memory=True,
            shared_memory=self.shared_memory
        )

    @agent
    def final_answer_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['final_answer_summarizer'],
            verbose=True,
            memory=True,
            shared_memory=self.shared_memory
        )

    @task
    def gather_business_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config['gather_business_intelligence_task'],
            agent=self.business_information_extractor(),
            shared_memory=self.shared_memory
        )

    @task
    def map_audience_demographics_task(self) -> Task:
        return Task(
            config=self.tasks_config['map_audience_demographics_task'],
            agent=self.audience_demographic_mapper(),
            shared_memory=self.shared_memory
        )

    @task
    def collect_market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['collect_market_research_task'],
            agent=self.market_research_fact_collector(),
            shared_memory=self.shared_memory
        )

    @task
    def analyze_competitor_meta_ads_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_competitor_meta_ads_task'],
            agent=self.competitor_snapshot_agent(),
            shared_memory=self.shared_memory
        )

    @task
    def define_brand_essence_task(self) -> Task:
        return Task(
            config=self.tasks_config['define_brand_essence_task'],
            agent=self.brand_essence_extractor(),
            shared_memory=self.shared_memory
        )

    @task
    def develop_meta_ad_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['develop_meta_ad_strategy_task'],
            agent=self.chief_marketing_strategist(),
            output_json=MarketStrategy,
            shared_memory=self.shared_memory
        )

    @task
    def create_ad_designs_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_ad_designs_task'],
            agent=self.creative_content_creator(),
            shared_memory=self.shared_memory
        )

    @task
    def craft_ad_copy_task(self) -> Task:
        return Task(
            config=self.tasks_config['craft_ad_copy_task'],
            agent=self.ad_copy_specialist(),
            shared_memory=self.shared_memory
        )

    @task
    def review_ad_designs_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_ad_designs_task'],
            agent=self.design_review_agent(),
            shared_memory=self.shared_memory
        )

    @task
    def optimize_campaign_feedback_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_campaign_feedback_task'],
            agent=self.strategic_feedback_coordinator(),
            shared_memory=self.shared_memory
        )

    @task
    def compile_final_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['compile_final_strategy_task'],
            agent=self.final_answer_summarizer(),
            context=[
                self.gather_business_intelligence_task(),
                self.map_audience_demographics_task(),
                self.collect_market_research_task(),
                self.analyze_competitor_meta_ads_task(),
                self.define_brand_essence_task(),
                self.develop_meta_ad_strategy_task(),
                self.create_ad_designs_task(),
                self.craft_ad_copy_task(),
                self.review_ad_designs_task(),
                self.optimize_campaign_feedback_task()
            ],
            shared_memory=self.shared_memory
        )

    def save_final_output(self, output_data, domain_name):
        """Saves the final output of the crew process."""
        print(f"Saving final output for domain: {domain_name}")
        with open(f"{domain_name}_final_output.txt", "w") as file:
            file.write(str(output_data))

    @crew
    def crew(self) -> Crew:
        """Creates the MarketingPosts crew"""
        marketing_crew = Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

        # Prepare input for the crew kickoff
        inputs = {
            "customer_domain": "mydailydefense.com",
            "project_description": "Daily Defense is a USA-based wellness brand offering a comprehensive range of dietary supplements and vitamins manufactured under GMP guidelines in FDA-registered facilities. Founded by Jenna Sabacheuskaya, the company focuses on boosting defenses from within through scientifically-formulated supplements targeting various health concerns including immunity, digestion, cognition, joint health, hormone balance, and aging support. Their product lineup includes both essential supplements like multivitamins and omega-3s and specialized formulas such as berberine complex and hormone support. The brand emphasizes quality control, using pure ingredients without artificial colors, preservatives, or sweeteners. Their development process involves collaboration with nutritionists, chemists, and naturopaths. Key brand differentiators include: Free shipping on all US orders, 30-day money-back guarantee, product bundles for cost savings, focus on natural ingredients, wide range of health categories covering 30+ different wellness areas, price points typically ranging from $24.95 to $39.95 per product, strong emphasis on cleanse/detox products as a core offering. The company positions itself as a premium yet accessible wellness brand, targeting health-conscious consumers looking for comprehensive supplementation solutions.",  # Example
        }

        # Run the crew process and save the output
        final_output = marketing_crew.kickoff(inputs=inputs)
        domain_name = inputs["customer_domain"]
        self.save_final_output(output_data=final_output, domain_name=domain_name)
        return marketing_crew
