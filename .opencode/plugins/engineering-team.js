/**
 * EngineeringTeam plugin for OpenCode.
 *
 * Registers this repository's shared skills directory. This intentionally does
 * not inject session-start bootstrap context; users invoke the skill manually.
 */

import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export const EngineeringTeamPlugin = async () => {
  const skillsDir = path.resolve(__dirname, '../../skills');

  return {
    config: async (config) => {
      config.skills = config.skills || {};
      config.skills.paths = config.skills.paths || [];
      if (!config.skills.paths.includes(skillsDir)) {
        config.skills.paths.push(skillsDir);
      }
    }
  };
};

export default EngineeringTeamPlugin;
