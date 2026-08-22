from client import AutonomousAgentGoalDecomposerClient

def main():
    client = AutonomousAgentGoalDecomposerClient()
    goal = 'Research top 5 AI coding tools and produce a comparison report for our product team'
    tools = ['web_search', 'database_query', 'document_writer', 'email_sender', 'code_executor']
    res = client.decompose_and_plan(goal, tools, 'research_analyst')
    print('Goal: ' + res['original_goal'])
    print('Agent: ' + res['agent_persona'] + ' | Total Steps: ' + str(res['estimated_total_steps']))
    print('Human Checkpoint: ' + str(res['human_checkpoint_required']))
    print('Critical Path: ' + str(res['critical_path']))
    print('Subgoals:')
    for sg in res['decomposed_subgoals']:
        print('  [' + sg['id'] + '] ' + sg['subgoal'] + ' | Tool: ' + sg['assigned_tool'] + ' | Steps: ' + str(sg['estimated_steps']))

if __name__ == '__main__':
    main()
